# Shell
Baseline: [Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html), ShellCheck and shfmt when configured.
- Declare the intended interpreter; use POSIX syntax for sh. Quote expansions, use arrays in Bash for argument vectors, and use -- before variable filenames where supported.
- Check command exit status explicitly; do not rely on set -e to handle every context. Use pipefail only with a supporting shell.
- Never eval untrusted text; keep secrets off command lines/logs. Check targets before deletion and require existing authorisation for destructive operations.
- Use mktemp and traps to clean up owned resources. Preserve useful exit codes and diagnostic stderr.
- Test success/failure/space-containing paths in isolated temporary fixtures with the existing runner (for example Bats). Run shellcheck and shfmt checks where available.
