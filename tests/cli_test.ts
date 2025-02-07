// edit
// plan
// review
// run

import { assertEquals, assertArrayIncludes, assertMatch } from "jsr:@std/assert";
import { assertSnapshot } from "jsr:@std/testing/snapshot";
import { $ } from "jsr:@david/dax"

const runbook = async (args: string[], config: { cwd: string }) => {
  const env = {
    WORKING_DIR: config.cwd,
  };
  const cmd = await $`runbook ${args}`.env(env).stdout("piped").stderr("piped").noThrow();
  return cmd;
};

const init = async (dir: string) => {
  const _cmd = await runbook(["init", "--skip-confirmation=true"], { cwd: dir });
};

const setup = async () => {
  const dir = await Deno.makeTempDir();
  await init(dir);
  return {runbook: (args: string[]) => runbook(args, { cwd: dir }), dir};
}

Deno.test.ignore("check", async (t) => {
  const {runbook } = await setup();
  const cmd = await runbook(["check", "runbooks/binder/_template-deno.ipynb"]);
  assertMatch(cmd.stdout.trim(), /Checked .*\/runbooks\/binder\/_template-deno\.ipynb/);
  assertMatch(cmd.stderr.trim(), /.*Check.*runbooks\/binder\/_template-deno-.*\.ts/);
  assertEquals(cmd.code, 0);
});

Deno.test("convert", async (t) => {
  const {runbook, dir} = await setup();
  const cmd = await runbook(["convert", "runbooks/binder/_template-deno.ipynb", "_template-deno.ts"]);
  assertSnapshot(t, { stderr: cmd.stderr, exitCode: cmd.code });
  const txt = await Deno.readTextFile([dir, "_template-deno.ts"].join("/"));
  assertSnapshot(t, txt);
});

// create
Deno.test("create", async (t) => {
  const {runbook, dir} = await setup();
  const cmd = await runbook(["create", "create-test.ipynb"]);
  assertSnapshot(t, { stderr: cmd.stderr, exitCode: cmd.code });
  const exists = await Deno.stat([dir, "runbooks/binder/create-test.ipynb"].join("/")).then(() => true).catch(() => false);
  assertEquals(exists, true);
});

// diff
Deno.test.ignore("diff", async (t) => {
  const {runbook, dir} = await setup();

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

  const cmd = await runbook(["diff", "notebook1.ipynb", "notebook2.ipynb"]);
  assertSnapshot(t, { stdout: cmd.stdout, stderr: cmd.stderr, exitCode: cmd.code });
});

Deno.test("init", async (t) => {
  const {dir} = await setup();
  const files = (await getAllFiles(dir)).map(f => f.replace(dir, "")).sort();
  assertEquals(files, [
    "/runbooks/binder/_template-deno.ipynb",
    "/runbooks/binder/_template-python.ipynb",
    "/runbooks/.runbook.json",
  ].sort());
});

Deno.test("list", async (t) => {
  const {runbook } = await setup();
  const cmd = await runbook(["list"]);
  assertSnapshot(t, { stdout: cmd.stdout, stderr: cmd.stderr, exitCode: cmd.code });
});

// show
Deno.test("show", async (t) => {
  const {runbook } = await setup();
  const cmd = await runbook(["show", "runbooks/binder/_template-deno.ipynb"]);
  assertSnapshot(t, { stdout: cmd.stdout, stderr: cmd.stderr, exitCode: cmd.code });
});

// plan
Deno.test("plan: prompter interface", async (t) => {
  const cwd = Deno.cwd();
  const {runbook, dir } = await setup();
  const cmd = await runbook(["plan", "runbooks/binder/_template-deno.ipynb", "--prompter", [cwd, "tests/fixtures/prompters/echoer"].join("/")]);
  assertEquals(cmd.code, 0);

  const files = await getAllFiles($.path(dir).join("runbooks/runs").toString());
  const planFile = files.find(f => f.endsWith("_template-deno/_template-deno.ipynb"));
  if(!planFile) {
    throw new Error("Plan file not found");
  }
  const json = await Deno.readTextFile(planFile);
  const plan = JSON.parse(json);
  const maybeParamCells = plan.cells.filter((c: any) => c.cell_type === "code" && c.metadata?.tags?.includes("injected-parameters"));
  assertEquals(maybeParamCells.length, 1);
  const paramCell = maybeParamCells[0];
  assertArrayIncludes(paramCell.source, [`server = "main.xargs.io";\n`, `arg = 1;\n`, `anArray = ["a", "b"];\n`]);
  // assertSnapshot(t, { stdout: cmd.stdout, stderr: cmd.stderr, exitCode: cmd.code });
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
  const {runbook, dir} = await setup();
  const cmd = await runbook(["run", "--no-interactive", "runbooks/binder/_template-deno.ipynb", "--output", "output.ipynb"]);
  assertSnapshot(t, { stdout: cmd.stdout, stderr: cmd.stderr, exitCode: cmd.code });
  const output = await Deno.readTextFile([dir, "output.ipynb"].join("/"));
  assertSnapshot(t, output);
});

// version
Deno.test("version", async (t) => {
  const {runbook } = await setup();
  const cmd = await runbook(["version"]);
  assertSnapshot(t, { stdout: cmd.stdout.split(":")[0], stderr: cmd.stderr, exitCode: cmd.code });
});

async function* walkFiles(dir: string): AsyncGenerator<string> {
  for await (const entry of Deno.readDir(dir)) {
    const path = `${dir}/${entry.name}`;
    if (entry.isDirectory) {
      yield* walkFiles(path);
    } else {
      yield path;
    }
  }
}

async function getAllFiles(dir: string): Promise<string[]> {
  const files = [];
  for await (const file of walkFiles(dir)) {
    files.push(file);
  }
  return files;
}

