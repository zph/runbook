import * as log from "jsr:@std/log";

export const timestampISOLocal = (date: Date) => {
  // subtract the offset from t
  const offset = date.getTime() - date.getTimezoneOffset() * 60 * 1000;
  // create shifted Date object
  const local = new Date(offset);
  // convert to ISO format string
  return local.toISOString();
};

// Using .cache to avoid spreading temporary files across the repo
// and to be clear that they're transient
export const fileHandler = new log.FileHandler("INFO", {
  filename: [
    // TODO: decide how to populate this
    Deno.env.get("RUNBOOK_DIR"),
    "runbooks",
    ".cache",
    "logs",
    "audit",
    "output.log",
  ].join("/"),
  formatter: (record) =>
    JSON.stringify({
      level: record.levelName,
      message: record.msg,
      ts: timestampISOLocal(record.datetime),
      name: record.loggerName,
      // Note this requires we use logs with only a type signature of `log.info("message", {})`
      // not variadric usage
      args: record.args[0],
    }),
});

log.setup({
  handlers: {
    // TODO: decide on re-enabling fileHandler
    // file: fileHandler,
    console: new log.ConsoleHandler("INFO"),
  },

  loggers: {
    default: {
      level: "INFO",
      handlers: ["console"],
    },
  },
});

export { log };
