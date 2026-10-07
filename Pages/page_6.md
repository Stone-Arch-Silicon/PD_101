# Lesson 6: Power distribution and physical-only cells

Inspect how supply connections reach standard cells and why some cells have no RTL equivalent.

> [!NOTE]
> Before you start: Complete [Lesson 5](page_5.md). Allow 90–150 minutes, plus tool runtime. Keep your work in `evidence/lesson06/`. Lab notes: [files/lab06](../files/lab06/).

## What you will learn

- [ ] You identified supply layers and physical-only cells.
- [ ] You distinguished connectivity checks from electrical analysis.

## Read first

[LibreLane power distribution networks](https://librelane.readthedocs.io/en/stable/usage/pdn.html): read the standard-cell grid section. [OpenROAD PDN documentation](https://openroad.readthedocs.io/en/latest/main/src/pdn/README.html): read the overview and terminology.

Read the named sections, not the whole manual. Write two sentences connecting the reading to this lesson's experiment before running it.

## Key ideas

The power distribution network (PDN) carries supply current through rings, straps, and rails. Tap cells provide well/substrate ties; endcaps protect row boundaries. Filler cells fill legal gaps, and decaps can support local supply stability. Signal routing must coexist with these structures. A visible stripe does not by itself prove supply connectivity or acceptable voltage drop.



## Lab

1. In the baseline GUI, hide signal nets and display the supply nets and relevant metal layers.
2. Locate tap/endcap insertion and PDN generation in the run directory. Record warnings and checks from those stages.
3. Trace a supply connection from an upper-layer strap to a standard-cell rail in the layout.
4. Add a screenshot and a short connectivity explanation to your run record. If IR-drop analysis is available, record its assumed current/activity and source locations before quoting its result.

## Exercises

1. **Warm-up:** Distinguish a clock net from a supply net.
2. **Core:** Find one physical-only cell in your run and explain its purpose.
3. **Stretch:** Explain why adding wider straps might improve resistance but make signal routing harder.

## Hints and worked answers

<details>
<summary>Open after attempting the exercises</summary>

Supply nets deliver current; clocks communicate timing edges. Wider metal generally reduces resistance but occupies routing resources. IR-drop numbers depend on the power model and boundary conditions; a visually connected grid is only the start of the investigation.

</details>

## Checkpoint

- [ ] You identified supply layers and physical-only cells.
- [ ] You distinguished connectivity checks from electrical analysis.

Submit the changed source/configuration, exact command, tool versions, relevant log or report excerpt, and a short explanation of the result. A screenshot supports your explanation; it does not replace the underlying report. Never submit an upstream figure as your own run.
