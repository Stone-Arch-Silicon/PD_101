# Lesson 10: DRC, LVS, and a signoff evidence package

Distinguish clean geometry, correct connectivity, and timing closure instead of reducing all three to “the tool passed.”

> [!NOTE]
> Before you start: Complete [Lesson 9](page_9.md). Allow 90–150 minutes, plus tool runtime. Keep your work in `evidence/lesson10/`. Lab notes: [files/lab10](../files/lab10/).

## What you will learn

- [ ] DRC, LVS, timing, and antenna have separate statuses.
- [ ] Missing checks and known limitations are explicit.

## Read first

[LibreLane built-in steps](https://librelane.readthedocs.io/en/stable/reference/step_config_vars.html): locate the Magic/KLayout DRC and Netgen LVS steps used by your release. [KLayout documentation](https://www.klayout.de/doc/manual/drc.html): read the DRC introduction.

Read the named sections, not the whole manual. Write two sentences connecting the reading to this lesson's experiment before running it.

## Key ideas

Design-rule checking (DRC) checks geometry against a rule deck. Layout-versus-schematic (LVS) compares extracted connectivity to the reference netlist. Static timing analysis checks delays against constraints and corners. None of these replaces functional verification, and no single educational flow result is a complete foundry tapeout approval.



## Lab

1. Complete `files/signoff_checklist.md` using your baseline run. Every row needs status, report path, and a short interpretation.
2. Open one DRC report and the LVS summary. If there are violations, inspect an actual marker or mismatch and classify it before suggesting a repair.
3. Check setup and hold across the enabled corners, not just the most attractive number.
4. Use “not run” for checks absent from the flow. Do not convert missing reports into zero violations.

## Exercises

1. **Warm-up:** Can a DRC-clean layout have incorrect connectivity?
2. **Core:** Explain what an LVS pass does and does not establish.
3. **Stretch:** Have a peer audit your evidence without seeing the GUI. Which missing metadata prevents reproduction?

## Hints and worked answers

<details>
<summary>Open after attempting the exercises</summary>

Yes. A disconnected or wrongly connected net may still obey geometric rules. LVS supports connectivity equivalence under the extraction/setup used; it does not prove the original RTL implements the intended behavior or that timing meets every required scenario.

</details>

## Checkpoint

- [ ] DRC, LVS, timing, and antenna have separate statuses.
- [ ] Missing checks and known limitations are explicit.

Submit the changed source/configuration, exact command, tool versions, relevant log or report excerpt, and a short explanation of the result. A screenshot supports your explanation; it does not replace the underlying report. Never submit an upstream figure as your own run.
