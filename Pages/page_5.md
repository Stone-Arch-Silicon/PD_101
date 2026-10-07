# Lesson 5: Floorplanning and utilization

Explore how core area and whitespace affect the room available for cells, clocks, power, and routing.

> [!NOTE]
> Before you start: Complete [Lesson 4](page_4.md). Allow 90–150 minutes, plus tool runtime. Keep your work in `evidence/lesson05/`. Lab notes: [files/lab05](../files/lab05/).

## What you will learn

- [ ] You saved two controlled utilization experiments.
- [ ] Your comparison separates die/core/cell area.

## Read first

[LibreLane newcomers tutorial](https://librelane.readthedocs.io/en/stable/getting_started/newcomers/index.html): inspect floorplan and pin-placement discussion. [OpenROAD Flow Tutorial](https://openroad-flow-scripts.readthedocs.io/en/latest/tutorials/FlowTutorial.html): read floorplanning and macro-placement sections; its screenshots are explanatory, while this course continues using LibreLane commands.

Read the named sections, not the whole manual. Write two sentences connecting the reading to this lesson's experiment before running it.

## Key ideas

Utilization compares standard-cell area with available core area under the tool's definition. A rough planning estimate is core area = cell area / utilization fraction. Lower utilization usually gives routing more room but may increase wire lengths. A tiny design can be limited by I/O and power-grid requirements rather than cell area.

![OpenROAD view with large macros and surrounding core area](https://openroad-flow-scripts.readthedocs.io/en/latest/_images/macro_place_full_view.webp "Use the large blocks and the space between them to reason about routing channels.")

Credit: [OpenROAD Flow Tutorial](https://openroad-flow-scripts.readthedocs.io/en/latest/tutorials/FlowTutorial.html), BSD-3-Clause. This is an upstream example, not a result from this course.

## Lab

1. Open a floorplan-stage ODB/DEF from the baseline using the documented GUI flow. Identify die, core, cell rows, and pins.
2. Run `python3 scripts/make_variant.py --util 30 --period 20` and inspect the generated JSON beside the baseline configuration.
3. Implement the printed variant configuration with LibreLane. Repeat at utilization 50, keeping the same clock target.
4. Compare core area, placement density, routed wire length (if reported), and DRC outcomes. Save both run IDs.

## Exercises

1. **Warm-up:** Estimate core area for 1,200 square micrometers of cells at 40% utilization.
2. **Core:** Explain why the measured area may differ from the estimate.
3. **Stretch:** Propose a macro placement with channels and access to pins; label it conceptual, since the PWM contains no SRAM macro.

## Hints and worked answers

<details>
<summary>Open after attempting the exercises</summary>

The estimate is 3,000 square micrometers. Row/site rounding, margins, physical-only cells, and flow-specific definitions affect actual dimensions. Do not transfer a large CPU screenshot's absolute dimensions to this tiny block.

</details>

## Checkpoint

- [ ] You saved two controlled utilization experiments.
- [ ] Your comparison separates die/core/cell area.

Submit the changed source/configuration, exact command, tool versions, relevant log or report excerpt, and a short explanation of the result. A screenshot supports your explanation; it does not replace the underlying report. Never submit an upstream figure as your own run.
