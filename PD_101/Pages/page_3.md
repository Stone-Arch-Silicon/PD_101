# Lesson 3: Libraries, synthesis, and area

Learn what the physical flow receives from synthesis and where its timing and geometry information comes from.

> [!NOTE]
> Before you start: Complete [Lesson 2](page_2.md). Allow 90–150 minutes, plus tool runtime. Keep your work in `evidence/lesson03/`. Lab notes: [files/lab03](../files/lab03/).

## What you will learn

- [ ] You can distinguish Liberty, LEF, netlist, and GDS.
- [ ] The area measurement names its stage and units.

## Read first

[SKY130 documentation](https://skywater-pdk.readthedocs.io/en/main/): browse the standard-cell library documentation. [LibreLane PDK guide](https://librelane.readthedocs.io/en/stable/usage/about_pdks.html): identify the configured PDK and standard-cell library. Use the reference navigation if a section moves.

Read the named sections, not the whole manual. Write two sentences connecting the reading to this lesson's experiment before running it.

## Key ideas

Liberty describes characterized timing/power behavior, LEF describes abstract geometry, and GDS supplies detailed geometry. These views must agree on cell and pin names. Cell area is not die area: whitespace, clock cells, routing, and physical-only cells also consume resources. Synthesis can remove logic whose outputs are unobserved.



## Lab

1. Inspect the baseline's resolved configuration and synthesis log. Record its PDK and standard-cell library, rather than assuming a tool default.
2. Find the mapped netlist and identify a flop, a combinational cell, and any tie cells.
3. Find those cells in the installed library's LEF and Liberty views. Record one cell's area and one pin's direction from the actual files.
4. Record mapped cell count and area in your run record. Distinguish this synthesis area from the later placed design area.

## Exercises

1. **Warm-up:** Which view is used for cell pin geometry: LEF or Liberty?
2. **Core:** Explain one cell name and identify its drive-strength suffix using the PDK documentation.
3. **Stretch:** Make a separate RTL variant with one output disconnected, synthesize it, and explain the area change. Keep the baseline intact.

## Hints and worked answers

<details>
<summary>Open after attempting the exercises</summary>

LEF supplies abstract geometry. A drive-strength suffix identifies a particular library implementation, not a universal current specification. Removing an output can make a logic cone unobservable and removable; a smaller netlist is not an optimization if required behavior was lost.

</details>

## Checkpoint

- [ ] You can distinguish Liberty, LEF, netlist, and GDS.
- [ ] The area measurement names its stage and units.

Submit the changed source/configuration, exact command, tool versions, relevant log or report excerpt, and a short explanation of the result. A screenshot supports your explanation; it does not replace the underlying report. Never submit an upstream figure as your own run.
