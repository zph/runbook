import { assertEquals } from "jsr:@std/assert";
import { SecureEnvironment } from "./secrets.ts";
import Shell from "./shell.ts";

Deno.test("redaction test", async () => {
  const se = new SecureEnvironment({
    "SERVICE_PASSWORD": async () => "AAAAAAAAAAAA",
    "SERVICE_USER": async () => "username",
  });

  const sh = await (new Shell(se)).load();
  assertEquals(
    sh.replaceSecrets("AAAAAAAAAAAA username"),
    `$SERVICE_PASSWORD $SERVICE_USER`,
  );
});

Deno.test("validation sanitization", async function (t): Promise<void> {
  const se = new SecureEnvironment({
    "SERVICE_PASSWORD": async () => "AAAAAAAAAAAA",
    "SERVICE_USER": async () => "username",
  });

  const sh = await (new Shell(se)).load();
  const result = await sh.run("echo $SERVICE_PASSWORD username");
  const expected =
    `$SERVICE_PASSWORD $SERVICE_USER`;
  await assertEquals(expected, result.stdout());
});
