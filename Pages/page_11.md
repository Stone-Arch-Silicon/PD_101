# Lesson 11: Controlled PPA experiments

Make a defensible area/timing tradeoff using a small experiment matrix.

> [!NOTE]
> Before you start: Complete [Lesson 10](page_10.md). Allow 90–150 minutes, plus tool runtime. Keep your work in `evidence/lesson11/`. Lab notes: [files/lab11](../files/lab11/).

## What you will learn

- [ ] Four configurations and all outcomes are recorded.
- [ ] The selected candidate meets the stated acceptance criteria.

## Read first

[LibreLane design configuration](https://librelane.readthedocs.io/en/stable/reference/configuration.html): read configuration resolution and path handling. Review the variable descriptions for `CLOCK_PERIOD` and `FP_CORE_UTIL` in the [built-in steps reference](https://librelane.readthedocs.io/en/stable/reference/step_config_vars.html).

Read the named sections, not the whole manual. Write two sentences connecting the reading to this lesson's experiment before running it.

## Key ideas

PPA means power, performance, and area. You can compare area and timing without claiming to have measured power. Power estimates depend on activity and operating conditions. A Pareto candidate is not worse in all chosen metrics than another feasible candidate. Failed runs remain data; quietly discarding them biases the result.



## Lab

1. Use `scripts/make_variant.py` to generate configurations for utilization 30/50 and period 20/30 ns. Inspect each generated file.
2. Implement all four configurations, preserving run directories and exact tool versions.
3. Fill `files/experiment_matrix.csv` with area, setup/hold slack and corner, DRC/LVS status, and runtime. Use metrics inventory to find actual report keys rather than guessing.
4. Reject candidates that fail required checks. Select among feasible runs and explain the tradeoff. If none pass, report that outcome and the next experiment.

## Exercises

1. **Warm-up:** Why is changing utilization and RTL together hard to interpret?
2. **Core:** Identify the best feasible area result and the best feasible timing result in your data.
3. **Stretch:** Add an activity-based power estimate, documenting stimulus, voltage, corner, and assumptions. Otherwise label power unmeasured.

## Hints and worked answers

<details>
<summary>Open after attempting the exercises</summary>

Multiple simultaneous changes obscure causality. Compare feasible candidates under consistent measurement conditions. Lower area with broken timing is not an acceptable winner for a timing-constrained goal. Power remains unmeasured until a documented analysis supplies it.

</details>

## Checkpoint

- [ ] Four configurations and all outcomes are recorded.
- [ ] The selected candidate meets the stated acceptance criteria.

Submit the changed source/configuration, exact command, tool versions, relevant log or report excerpt, and a short explanation of the result. A screenshot supports your explanation; it does not replace the underlying report. Never submit an upstream figure as your own run.
