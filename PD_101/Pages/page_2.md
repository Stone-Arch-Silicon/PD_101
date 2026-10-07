# Lesson 2: A verified design and a reproducible baseline

Take the PWM capstone from RTL_101 into a small physical-design project without redesigning its behavior.

> [!NOTE]
> Before you start: Complete [Lesson 1](page_1.md). Allow 90–150 minutes, plus tool runtime. Keep your work in `evidence/lesson02/`. Lab notes: [files/lab02](../files/lab02/).

## What you will learn

- [ ] The reference PWM simulation passes.
- [ ] The baseline records configuration, tool/PDK revisions, and report paths.

## Read first

[LibreLane newcomers tutorial](https://librelane.readthedocs.io/en/stable/getting_started/newcomers/index.html): read “Configuration” and “Run directory”. Read the [RTL_101 PWM source](https://github.com/Stone-Arch-Silicon/RTL_101/tree/main/files/lab12) for the original interface.

Read the named sections, not the whole manual. Write two sentences connecting the reading to this lesson's experiment before running it.

## Key ideas

A baseline is the unchanged run against which experiments are compared. The supplied PWM captures a new duty value at a period boundary. Its top-level reset is synchronous and active low. Unused Tiny Tapeout pins remain in the interface; this standalone exercise does not include a pad ring or shuttle integration.



## Lab

From the repository root:

```bash
python3 scripts/run_sim.py
librelane files/design/config.json
librelane --last-run --flow openinklayout files/design/config.json
```

The first command requires `iverilog` and `vvp`. Read `files/design/config.json`; identify the top, RTL path, clock port, and clock period. Save the simulation result before running implementation. Start `files/run_record.md` for the baseline; copy it into your evidence directory. Locate the final reports and record timing and physical checks as reported, including failures.

## Exercises

1. **Warm-up:** Convert a 20 ns period to MHz.
2. **Core:** Explain why changing `CLOCK_PERIOD` does not change the PWM RTL's logical period in cycles.
3. **Stretch:** Add a duty-cycle test at value 127 and show the result before any implementation change.

## Hints and worked answers

<details>
<summary>Open after attempting the exercises</summary>

20 ns corresponds to 50 MHz. The counter still wraps every 256 cycles; clock frequency changes the duration of those cycles. The registered comparator introduces a cycle alignment that your test must respect. Do not expect a new duty value to take effect immediately.

</details>

## Checkpoint

- [ ] The reference PWM simulation passes.
- [ ] The baseline records configuration, tool/PDK revisions, and report paths.

Submit the changed source/configuration, exact command, tool versions, relevant log or report excerpt, and a short explanation of the result. A screenshot supports your explanation; it does not replace the underlying report. Never submit an upstream figure as your own run.

![Physical implementation stages](../assets/flow.svg "Each stage produces artifacts to inspect; final geometry is only one output.")

Credit: original Stone Arch Silicon teaching diagram.
