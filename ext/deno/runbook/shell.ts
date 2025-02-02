import {
  build$,
  CommandBuilder,
  CommandContext,
  CommandResult,
} from "dax";
import { log, fileHandler, timestampISOLocal } from "./log.ts";
import { ulid } from "jsr:@std/ulid@1";
import { CommandResultStub, SecureCommandResultParams } from "./shell.d.ts";
import { SecureEnvironment } from "./secrets.ts";
import { RunOptions } from "./shell.d.ts";

export const RunOptionsDefaults = {
  stdin: "",
  verbose: false,
  noThrow: false,
  dryRun: false,
  isSensitive: true,
};

export class SecureCommandResult {
  id: string;
  timing: {
    duration_ms: number;
    start: string;
    end: string;
  };
  ts: string;
  code: number;
  command: string;
  #stdout: string;
  #stderr: string;
  constructor(
    { timing, ts, code, command, stdout, stderr }: SecureCommandResultParams,
  ) {
    this.id = ulid();
    this.timing = timing;
    this.ts = ts;
    this.code = code;
    this.command = command;
    this.#stdout = stdout;
    this.#stderr = stderr;
  }

  stdout(): string {
    return this.#stdout;
  }

  // deno-lint-ignore no-explicit-any
  json(): { [key: string]: any } | [any] {
    return JSON.parse(this.#stdout);
  }

  stderr(): string {
    return this.#stderr;
  }
}

const htmlWarning = (
  message: string,
  command: string,
  stderr: string,
) => {
  return `
<html>
<head>
<style>
  .warning {
    background-color: red;
    border: 5px solid black;
    padding: 20px;
    text-align: center;
  }
</style>
</head>
<body>

<div class="warning">
  <table>
  <tr>
    <th>Message: ${message}</th>
    <th>Command: <code>${command}</code></th>
    <th>Stderr: <code>${stderr}</code></th>
  </tr>
  </table>
</div>

</body>
</html>`;
};

/*
 * Safe helper to ensure that this function succeeds
 * even when Deno.jupyter is unavailable such as inside
 * the `deno repl`
    await jupyterBroadcast("display_data", {
        data: { "application/json": to_broadcast},
        metadata: {},
      transient: { display_id: "progress" }
    })
*/

// deno-lint-ignore no-explicit-any
const jupyterBroadcast = async (msg: string, options: any) => {
  if (Deno.jupyter != undefined) {
    await Deno.jupyter.broadcast(msg, options);
  }
};

export default class Shell {
  #secureEnvironment: SecureEnvironment;
  #secrets: { [key: string]: string };

  constructor(secrets: SecureEnvironment) {
    this.#secureEnvironment = secrets;
    this.#secrets = {};
  }

  async load(): Promise<Shell> {
    const secrets = await this.#secureEnvironment.load();
    this.#secrets = secrets;
    return this;
  }

  async execution(
    unsafeCommand: string,
    { stdin, noThrow }: RunOptions = {
      stdin: "",
      verbose: false,
      noThrow: false,
    },
  ): Promise<SecureCommandResult> {
    const commandBuilder = new CommandBuilder()
      .stdout("inheritPiped")
      .stderr("inheritPiped")
      .env(this.#secrets);

    if (stdin == null) {
      stdin = "";
    }

    const $$ = build$({ commandBuilder });

    try {
      const safeCommand = this.replaceSecrets(unsafeCommand);
      // Intentionally print to console for the sake of jupyter display
      console.log(`> ${safeCommand}`);
      const executor = $$.raw`${unsafeCommand}`.stdinText(stdin).noThrow(
        noThrow,
      );
      const rawResponse = await executor;
      return this.redactor(unsafeCommand, rawResponse);
    } catch (e) {
      log.error("SECURE_EXECUTION", e);
      const a: CommandResultStub = {
        stdout: "",
        stderr: e.message,
        code: 1,
      };
      return this.redactor(unsafeCommand, a);
    }
  }

  // Pass in per-run env values that are merged over #secrets
  // Replaces plaintext secrets with their secret names
  replaceSecrets(text: string): string {
    for (const [k, v] of Object.entries(this.#secrets)) {
      text = text.replaceAll(v, `$${k}`);
    }
    return text;
  }

  redactor(
    args: string,
    result: CommandResult | CommandResultStub,
  ): SecureCommandResult {
    const { stdout, stderr, code } = result;

    return new SecureCommandResult({
      timing: {
        duration_ms: 0,
        start: "",
        end: "",
      },
      ts: "",
      code,
      command: this.replaceSecrets(args),
      stdout: this.replaceSecrets(stdout).trimEnd(),
      stderr: this.replaceSecrets(stderr),
    });
  }

  async run(
    cmd: string,
    options: RunOptions = RunOptionsDefaults,
  ): Promise<SecureCommandResult> {
    const start = (new Date()).toISOString();
    performance.mark("command_start");
    const r: SecureCommandResult = await this.execution(cmd, options);
    // Unset cmd and options to avoid logging the command in the output due to containing
    // secrets
    cmd = "";

    // Variables from here forward must be sanitized to avoid secrets appearing in logs
    performance.mark("command_end");
    const end = (new Date()).toISOString();
    const measure = performance.measure(
      "command",
      "command_start",
      "command_end",
    );
    const timing = {
      duration_ms: Math.round(measure.duration * 1000) / 1000,
      start,
      end,
    };
    r.timing = timing;
    r.ts = timestampISOLocal(new Date());

    if (options.verbose) {
      await jupyterBroadcast("display_data", {
        data: { "application/json": r },
        metadata: {},
        transient: { display_id: "progress" },
      });
    }
    log.info("SHELL", r);

    // Flush the file handler to ensure that the logs are written to disk
    fileHandler.flush();
    if (r.code != 0) {
      log.error("EXIT DUE TO NON_ZERO EXIT CODE", { id: r.id });
      fileHandler.flush();
      await jupyterBroadcast("display_data", {
        data: {
          "text/html": htmlWarning(
            `Exiting due to nonzero exit code`,
            r.command,
            r.stderr(),
          ),
        },
        metadata: {},
        transient: { display_id: "progress" },
      });
      if (!options.noThrow) {
        throw new Error("Exiting due to non-zero exit code");
      }
    }

    // Return broadcast including stdout / stderr to operator
    return r;
  }

  /*
   * bastion(command, {stdin: "textual representation of a config file \n more lines"})
   * provides a helper mechanism for two scenarios
   * - using command on bastion normally via ssh/ssm/teleport
   * - using shell on bastion in cases where you need to have a config file on bastion but don't want it on disk because of sensitive data
   *   this helper avoids the complexity and risk of encrypting and passing around keys because the config file can exist exclusively in memory
   * bastion fn will pipe the text of the config file in as stdin to ssh which will be accessible as /dev/stdin file descriptor

    > await bastion(`uname -a`)
    > await bastion(`head -2 /dev/stdin`, {stdin: "textual representation of a config file \n more lines"})
    > await bastion(`a-command -config /dev/stdin`, {stdin: "textual representation of a config file \n more lines"})
  */
  bastion = async (
    cmd: string,
    options: RunOptions = RunOptionsDefaults,
  ): Promise<SecureCommandResult> => {
    throw Error(`Not implemented, extend Shell class with a custom implementation. this.run is available if the command starts as a local shell`)

    // Example but realize you'll need to handle quoting levels
    cmd = `ssh bastion "${cmd}"`

    // Note that if we need to pass binary values it should be as Uint8Array and with `stdin(array)` not `stdinText(text)`
    return await this.run(cmd, options);
  };
}
