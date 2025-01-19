import { assertEquals } from "jsr:@std/assert";
import { assertSnapshot } from "jsr:@std/testing/snapshot";
import { $ } from "jsr:@david/dax"

const runbook = async (args: string[], config: { cwd: string }) => {
  const env = {
    WORKING_DIR: config.cwd,
  };
  const cmd = await $`WORKING_DIR=${config.cwd} runbook ${args}`.env(env).stdout("piped").stderr("piped").noThrow().printCommand();
  return cmd;
};

const init = async (dir: string) => {
  const _cmd = await runbook(["init", "--skip-confirmation=true"], { cwd: dir });
};

Deno.test("check", async (t) => {
  const cmd = await runbook(["check", "runbooks/binder/_template-deno.ipynb"], { cwd: Deno.cwd() });
  assertSnapshot(t, { exitCode: cmd.code, stdout: cmd.stdout, stderrEndsWith: cmd.stderr.trim().endsWith(".ts") });
});

Deno.test("list", async (t) => {
  const dir = await Deno.makeTempDir();
  await init(dir);
  const cmd = await runbook(["list"], { cwd: dir });
  assertSnapshot(t, { stdout: cmd.stdout, stderr: cmd.stderr, exitCode: cmd.code });
});

Deno.test("convert", async (t) => {
  const dir = await Deno.makeTempDir();
  await init(dir);
  const cmd = await runbook(["convert", "runbooks/binder/_template-deno.ipynb", "_template-deno.ts"], { cwd: dir });
  assertSnapshot(t, { stderr: cmd.stderr, exitCode: cmd.code });
  const txt = await Deno.readTextFile([dir, "_template-deno.ts"].join("/"));
  assertSnapshot(t, txt);
});
