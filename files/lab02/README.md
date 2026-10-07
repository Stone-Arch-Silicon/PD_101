# Lab 02: A verified design and a reproducible baseline

[Read the lesson](../../Pages/page_2.md).

From the repository root:

```bash
python3 scripts/run_sim.py
librelane files/design/config.json
librelane --last-run --flow openinklayout files/design/config.json
```

The first command requires `iverilog` and `vvp`. Read `files/design/config.json`; identify the top, RTL path, clock port, and clock period. Save the simulation result before running implementation. Start `files/run_record.md` for the baseline; copy it into your evidence directory. Locate the final reports and record timing and physical checks as reported, including failures.

## Acceptance

- [ ] The reference PWM simulation passes.
- [ ] The baseline records configuration, tool/PDK revisions, and report paths.
