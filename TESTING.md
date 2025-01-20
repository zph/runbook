# Testing

## Coverage

| Command | Description                                                | Unit/Integration Tests | Manual Testing Required |
| ------- | ---------------------------------------------------------- | ---------------------- | ----------------------- |
| check   | Check language validity and formatting of a notebook       | ✅                     | ❌                      |
| convert | Convert an existing runbook to different format            | ✅                     | ❌                      |
| create  | Create a new runbook from [template]                       | ✅                     | ❌                      |
| diff    | Diff two notebooks                                         | ✅                     | ❌                      |
| edit    | Edit an existing runbook                                   | ❌                     | ✅️                      |
| init    | Initialize a folder as a runbook repository                | ✅                     | ❌                      |
| list    | List runbooks                                              | ✅                     | ❌                      |
| plan    | Prepares the runbook for execution by injecting parameters | ✅                     | ❌️                      |
| review  | [Unimplemented] Entrypoint for reviewing runbook           | ❌                     | N/A                     |
| run     | Run a notebook                                             | ❌                     | ✅️                      |
| show    | Show runbook parameters and metadata                       | ✅                     | ❌                      |
| version | Display version information about runbook                  | ✅                     | ❌                      |

Commands marked with "Manual Testing Required: Yes" should be tested manually as
they cannot be easily automation tested.

## Manual Testing

See `tests/manual` for manual testing.

It involves running the shell scripts in `tests/manual` and auditing behavior.
