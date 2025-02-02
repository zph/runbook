import { $ } from "jsr:@david/dax";

export async function getTokenFromVaultByPath(path: string) {
  const hasOp = await $.which("op");
  if (hasOp) {
    const result = await $
      .raw`op read "${path}"`
      .text();
    return result.trim();
  } else {
    throw new Error(
      "No way to get slack token from vault. Appears that 1password cli is failing. See 1password cli setup instructions and Try again.",
    );
  }
}
