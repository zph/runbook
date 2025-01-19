# Testing

## CLI

| Command | Description                                                | Unit Tests | Manual Testing Required               |
| ------- | ---------------------------------------------------------- | ---------- | ------------------------------------- |
| check   | Check language validity and formatting of a notebook       | ✅         | No                                    |
| convert | Convert an existing runbook to different format            | ✅         | Yes - Test conversion between formats |
| create  | Create a new runbook from [template]                       | ✅         | Yes - Verify template rendering       |
| diff    | Diff two notebooks                                         | ✅         | Yes - Visual verification             |
| edit    | Edit an existing runbook                                   | ✅         | Yes - Interactive editing             |
| init    | Initialize a folder as a runbook repository                | ✅         | No                                    |
| list    | List runbooks                                              | ✅         | No                                    |
| plan    | Prepares the runbook for execution by injecting parameters | ❌         | Yes - Parameter injection             |
| review  | [Unimplemented] Entrypoint for reviewing runbook           | ❌         | N/A                                   |
| run     | Run a notebook                                             | ✅         | Yes - Full execution                  |
| show    | Show runbook parameters and metadata                       | ✅         | No                                    |
| version | Display version information about runbook                  | ✅         | No                                    |

Commands marked with "Manual Testing Required: Yes" should be tested manually as
they cannot be easily automation tested. Key areas to verify:

- `convert`: Test conversion between all supported formats
- `create`: Verify template rendering and parameter substitution
- `diff`: Visually verify diff output is correct
- `edit`: Test interactive editing workflow
- `plan`: Verify parameter injection and validation
- `run`: Test full execution with various parameter combinations
