# systemd units

Baseline: [systemd.service](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html), [systemd.exec](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html), and [systemd.unit](https://www.freedesktop.org/software/systemd/man/latest/systemd.unit.html).

- Keep directives under their correct `[Unit]`, `[Service]`, or `[Install]` section. Use one explicit `ExecStart=` for a long-running service and keep arguments readable.
- Use drop-ins for local overrides. Clear a list-valued directive before replacing it, and inspect the effective unit with `systemctl --user cat` or `systemctl --user show`.
- Keep secrets in protected credential or environment files, not in source-controlled units. Preserve existing sandbox and write-path restrictions.
- Validate changed files with `systemd-analyze verify`, reload the user manager, restart the affected service, and inspect status and recent logs. Keep a copy of the prior unit for rollback.
