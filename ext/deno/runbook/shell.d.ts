export interface SecureCommandResultParams {
  timing: {
    duration_ms: number;
    start: string;
    end: string;
  };
  ts: string;
  code: number;
  command: string;
  stdout: string;
  stderr: string;
}

export interface SecureCommandResultRaw {
  // stdout is the output of the command with trimEnd() applied
  stdout: string;
  stderr: string;
  code: number;
  command: string;
}

export type RunOptions = {
  stdin?: string;
  verbose?: boolean;
  // TODO(zph): thread this through
  //env?: SecureEnvironment;
  noThrow?: boolean;
  dryRun?: boolean;
};

export interface CommandResultStub {
  stdout: string;
  stderr: string;
  code: number;
}
