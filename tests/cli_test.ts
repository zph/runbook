// edit
// plan
// review
// run

import { assertEquals } from "jsr:@std/assert";
import { assertSnapshot } from "jsr:@std/testing/snapshot";
import { $ } from "jsr:@david/dax"

const runbook = async (args: string[], config: { cwd: string }) => {
  const env = {
    WORKING_DIR: config.cwd,
  };
  const cmd = await $`WORKING_DIR=${config.cwd} runbook ${args}`.env(env).stdout("piped").stderr("piped").noThrow();
  return cmd;
};

const init = async (dir: string) => {
  const _cmd = await runbook(["init", "--skip-confirmation=true"], { cwd: dir });
};

const setup = async () => {
  const dir = await Deno.makeTempDir();
  await init(dir);
  return dir;
}

Deno.test("check", async (t) => {
  const dir = await setup();
  const cmd = await runbook(["check", "runbooks/binder/_template-deno.ipynb"], { cwd: dir });
  assertSnapshot(t, { exitCode: cmd.code, stdoutEndsWith: cmd.stdout.trim().endsWith("runbooks/binder/_template-deno.ipynb"), stderrEndsWith: cmd.stderr.trim().endsWith(".ts") });
});

Deno.test("convert", async (t) => {
  const dir = await setup();
  const cmd = await runbook(["convert", "runbooks/binder/_template-deno.ipynb", "_template-deno.ts"], { cwd: dir });
  assertSnapshot(t, { stderr: cmd.stderr, exitCode: cmd.code });
  const txt = await Deno.readTextFile([dir, "_template-deno.ts"].join("/"));
  assertSnapshot(t, txt);
});

// create
Deno.test("create", async (t) => {
  const dir = await setup();
  const cmd = await runbook(["create", "create-test.ipynb"], { cwd: dir });
  assertSnapshot(t, { stderr: cmd.stderr, exitCode: cmd.code });
  const exists = await Deno.stat([dir, "runbooks/binder/create-test.ipynb"].join("/")).then(() => true).catch(() => false);
  assertEquals(exists, true);
});

// diff
Deno.test.ignore("diff", async (t) => {
  const dir = await setup();

  // Create two notebooks with different content
  await Deno.writeTextFile(
    [dir, "notebook1.ipynb"].join("/"),
    JSON.stringify({
      cells: [{
        cell_type: "code",
        source: "print('hello')",
        outputs: []
      }]
    })
  );

  await Deno.writeTextFile(
    [dir, "notebook2.ipynb"].join("/"),
    JSON.stringify({
      cells: [{
        cell_type: "code",
        source: "print('world')",
        outputs: []
      }]
    })
  );

  const cmd = await runbook(["diff", "notebook1.ipynb", "notebook2.ipynb"], { cwd: dir });
  assertSnapshot(t, { stdout: cmd.stdout, stderr: cmd.stderr, exitCode: cmd.code });
});

Deno.test("init", async (t) => {
  const dir = await setup();
  const files = await Array.fromAsync(Deno.readDir(dir));
  const filenames = files.map(f => f.name).sort();
  assertSnapshot(t, filenames);
});

Deno.test("list", async (t) => {
  const dir = await setup();
  const cmd = await runbook(["list"], { cwd: dir });
  assertSnapshot(t, { stdout: cmd.stdout, stderr: cmd.stderr, exitCode: cmd.code });
});

// show
Deno.test("show", async (t) => {
  const dir = await setup();
  const cmd = await runbook(["show", "runbooks/binder/_template-deno.ipynb"], { cwd: dir });
  assertSnapshot(t, { stdout: cmd.stdout, stderr: cmd.stderr, exitCode: cmd.code });
});

// run
/* failing on nested dax commands
Exception encountered at "In [3]":
Stack trace:
Error: Exited with code: 128
    at CommandChild.pipedStdoutBuffer (https://deno.land/x/dax@0.39.2/src/command.ts:758:19)
    at eventLoopTick (ext:core/01_core.js:175:7)
*/
Deno.test.ignore("run", async (t) => {
  const dir = await setup();
  const cmd = await runbook(["run", "--no-interactive", "runbooks/binder/_template-deno.ipynb", "--output", "output.ipynb"], { cwd: dir });
  assertSnapshot(t, { stdout: cmd.stdout, stderr: cmd.stderr, exitCode: cmd.code });
  const output = await Deno.readTextFile([dir, "output.ipynb"].join("/"));
  assertSnapshot(t, output);
});

// version
Deno.test("version", async (t) => {
  const dir = await setup();
  const cmd = await runbook(["version"], { cwd: dir });
  assertSnapshot(t, { stdout: cmd.stdout.split(":")[0], stderr: cmd.stderr, exitCode: cmd.code });
});
