export interface Secrets {
  [key: string]: () => Promise<string>;
}

export class SecureEnvironment {
  #secrets: Secrets;
  constructor(secrets: Secrets) {
    this.#secrets = secrets;
  }

  async load(): Promise<{ [key: string]: string }> {
    const acc: { [key: string]: string } = {};
    for await (const [k, v] of Object.entries(this.#secrets)) {
      const resolved = await v();
      acc[k] = resolved;
    }

    // Ensure that we don't have overlapping secret keys
    // because they will have undefined behavior during
    // replacements
    this.ensureNonOverlappingKeys(acc);
    return acc;
  }

  ensureNonOverlappingKeys(kvs: { [key: string]: string }) {
    const keys = Object.keys(kvs);
    keys.forEach((key, _i) => {
      keys.forEach((kx, _ix) => {
        if (kx.includes(key) && key !== kx) {
          throw new Error(`Secrets cannot overlap: ${key} and ${kx}`);
        }
      });
    });
  }
}
