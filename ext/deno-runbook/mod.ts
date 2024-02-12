// Mod.ts for runbook-deno helpers
// Default Setup
// See deno dax module for capabilities, including $.request, retry, etc
import {CommandBuilder, build$} from "https://deno.land/x/dax/mod.ts";

const commandBuilder = new CommandBuilder()
  .stdout("inheritPiped")
  .stderr("inheritPiped")
  .printCommand(true);

const $ = build$({ commandBuilder });

const sh = async (...args) => {
    const start = (new Date()).toISOString()
    performance.mark('command_start');
    const r = await $.raw`${args.join(" ")}`
    performance.mark('command_end')
    const end = (new Date()).toISOString()
    const measure = performance.measure('command', 'command_start', 'command_end')
    const timing = {duration_ms: measure.duration, start, end}
    const {stdout, stderr, code} = r
    await Deno.jupyter.broadcast("display_data", {
        data: { "application/json": {command: args.join(" "), exit_code: code, timing, stdout, stderr}},
        metadata: {},
      transient: { display_id: "progress" }
    });
    return r
}

export { sh, $ }
