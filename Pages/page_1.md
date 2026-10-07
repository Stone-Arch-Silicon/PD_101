# Lesson 1: Tools and the RTL-to-GDS journey

Set up a reproducible environment and inspect a real reference layout before changing any flow settings.

> [!NOTE]
> Before you start: Complete RTL_101 through sequential logic and synthesis. Allow 90–150 minutes, plus tool runtime. Keep your work in `evidence/lesson01/`. Lab notes: [files/lab01](../files/lab01/).

## What you will learn

- [ ] The smoke test completes and versions are recorded.
- [ ] You can locate and explain the reference run artifacts.

## Read first

[LibreLane installation](https://librelane.readthedocs.io/en/stable/installation/index.html): choose the supported path for your OS. Then read “Installation”, “Running the default flow”, and “Checking the results” in the [newcomers tutorial](https://librelane.readthedocs.io/en/stable/getting_started/newcomers/index.html). Follow upstream setup commands rather than an old OpenLane 1 tutorial.

Read the named sections, not the whole manual. Write two sentences connecting the reading to this lesson's experiment before running it.

## Key ideas

RTL describes behavior. Synthesis produces a cell netlist; placement assigns locations; clock-tree synthesis distributes the clock; routing connects pins. Extraction estimates wire parasitics, and signoff checks the result. A GDS file is geometry, not evidence that the design satisfies its constraints. Record the flow release and PDK revision so another student can reproduce your experiment.

![KLayout showing the routed pm32 example](https://librelane.readthedocs.io/en/stable/_images/pm32-gds.webp "An upstream final layout: zoom in to distinguish cells, wires, and the power grid.")

Credit: [LibreLane newcomers tutorial](https://librelane.readthedocs.io/en/stable/getting_started/newcomers/index.html), Apache-2.0. This is an upstream example, not a result from this course.

## Lab

1. Install LibreLane using the assigned guide, including its environment activation. Windows students use the Linux/WSL path documented upstream.
2. Run the documented smoke test. Save the full log and `librelane --version` in your evidence directory.
3. Complete the upstream pm32 example unchanged. Open its layout using the documented KLayout command.
4. Identify the run directory, resolved configuration, a timing report, and final GDS. Record their actual paths; step numbers can change across releases.
5. Clone this repository and run `python3 scripts/check_course.py`.

## Exercises

1. **Warm-up:** Put synthesis, routing, placement, and extraction in dependency order.
2. **Core:** Annotate a screenshot of your pm32 run with core boundary, cells, and metal. Explain what the screenshot cannot prove.
3. **Stretch:** Compare one intermediate DEF/ODB with the final GDS. Why are both useful?

## Hints and worked answers

<details>
<summary>Open after attempting the exercises</summary>

Synthesis precedes placement, routing, and extraction. DEF/ODB retain implementation information useful to the tools; GDS describes mask geometry. A plausible picture does not establish timing, connectivity equivalence, or design-rule compliance.

</details>

## Checkpoint

- [ ] The smoke test completes and versions are recorded.
- [ ] You can locate and explain the reference run artifacts.

Submit the changed source/configuration, exact command, tool versions, relevant log or report excerpt, and a short explanation of the result. A screenshot supports your explanation; it does not replace the underlying report. Never submit an upstream figure as your own run.
