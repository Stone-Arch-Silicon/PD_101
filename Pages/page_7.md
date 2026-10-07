# Lesson 7: Placement, congestion, and optimization

Look beyond a legal placement to determine whether it is likely to route and meet timing.

> [!NOTE]
> Before you start: Complete [Lesson 6](page_6.md). Allow 90–150 minutes, plus tool runtime. Keep your work in `evidence/lesson07/`. Lab notes: [files/lab07](../files/lab07/).

## What you will learn

- [ ] You can identify legal placement versus routing congestion.
- [ ] Your optimization claim cites before/after reports.

## Read first

[OpenROAD global placement](https://openroad.readthedocs.io/en/latest/main/src/gpl/README.html): overview. [OpenROAD detailed placement](https://openroad.readthedocs.io/en/latest/main/src/dpl/README.html): overview. Use the [Flow Tutorial](https://openroad-flow-scripts.readthedocs.io/en/latest/tutorials/FlowTutorial.html) to interpret GUI views.

Read the named sections, not the whole manual. Write two sentences connecting the reading to this lesson's experiment before running it.

## Key ideas

Global placement searches for good approximate locations. Detailed placement legalizes cells onto sites while respecting overlap and placement rules. Congestion measures competition for routing capacity; it is not the same thing as cell density. Optimization can resize cells or insert buffers, so post-placement cell counts need not match synthesis.



## Lab

1. Inspect the global- and detailed-placement artifacts in your baseline run.
2. In the GUI, inspect density and congestion views if available. Record which stage each view represents.
3. Compare the two utilization runs from Lesson 5. Find the worst region and explain whether pins, cell clusters, or the power grid could contribute.
4. Compare area and timing before and after placement optimization. Use `python3 scripts/metrics.py PATH_TO_RUN` to inventory numeric metrics and their source files.

## Exercises

1. **Warm-up:** Can a placement have no overlaps yet be unroutable?
2. **Core:** Find evidence of buffer insertion or cell resizing in one log.
3. **Stretch:** Predict how spreading cells might change both congestion and path delay, then test one change.

## Hints and worked answers

<details>
<summary>Open after attempting the exercises</summary>

Yes: legal placement does not guarantee enough tracks for all nets. Spreading reduces local competition but may lengthen wires. A useful experiment changes one variable and records both its benefit and its cost.

</details>

## Checkpoint

- [ ] You can identify legal placement versus routing congestion.
- [ ] Your optimization claim cites before/after reports.

Submit the changed source/configuration, exact command, tool versions, relevant log or report excerpt, and a short explanation of the result. A screenshot supports your explanation; it does not replace the underlying report. Never submit an upstream figure as your own run.
