# Lesson 9: Routing, antenna, and extraction

Follow the transition from estimated connections to actual wires and parasitic timing.

> [!NOTE]
> Before you start: Complete [Lesson 8](page_8.md). Allow 90–150 minutes, plus tool runtime. Keep your work in `evidence/lesson09/`. Lab notes: [files/lab09](../files/lab09/).

## What you will learn

- [ ] You inspected real wires/vias and extracted timing.
- [ ] You recorded antenna and routing checks separately.

## Read first

[OpenROAD global routing](https://openroad.readthedocs.io/en/latest/main/src/grt/README.html), [detailed routing](https://openroad.readthedocs.io/en/latest/main/src/drt/README.html), and [parasitic extraction](https://openroad.readthedocs.io/en/latest/main/src/rcx/README.html): read the introductory sections only.

Read the named sections, not the whole manual. Write two sentences connecting the reading to this lesson's experiment before running it.

## Key ideas

Global routing allocates approximate routes and resources. Detailed routing chooses legal wires and vias. Antenna checks address fabrication charging damage; they are not about wireless antennas. Extraction estimates resistance and capacitance of routed interconnect, which alters path delays. A pre-route timing result is not a post-route result.



## Lab

1. Locate global routing, detailed routing, antenna checking, and extraction in the baseline log.
2. Inspect a routed net across layers, including its vias. Capture a close-up with a layer legend.
3. Compare pre-route estimated timing and post-route extracted timing. Record the corners and report types so the comparison is meaningful.
4. Inventory the final parasitic, netlist, and geometry artifacts. Record routing/antenna violations even when the flow generated a GDS file.

## Exercises

1. **Warm-up:** Why can routing introduce a timing failure after placement passed?
2. **Core:** Explain one antenna repair mechanism using the upstream documentation.
3. **Stretch:** For a path dominated by wire delay, propose a placement or buffering experiment and predict its area cost.

## Hints and worked answers

<details>
<summary>Open after attempting the exercises</summary>

Real wires and vias add resistance and capacitance that estimates may miss. Depending on the process and flow, antenna repair may use diodes or routing changes. Buffering can reduce a long interconnect delay at the cost of cell area, power, and additional nets.

</details>

## Checkpoint

- [ ] You inspected real wires/vias and extracted timing.
- [ ] You recorded antenna and routing checks separately.

Submit the changed source/configuration, exact command, tool versions, relevant log or report excerpt, and a short explanation of the result. A screenshot supports your explanation; it does not replace the underlying report. Never submit an upstream figure as your own run.
