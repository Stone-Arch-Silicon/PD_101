# Lesson 12: Capstone: reviewable physical-design handoff

Package a small implementation so a teammate can rerun it and review the evidence.

> [!NOTE]
> Before you start: Complete [Lesson 11](page_11.md). Allow 90–150 minutes, plus tool runtime. Keep your work in `evidence/lesson12/`. Lab notes: [files/lab12](../files/lab12/).

## What you will learn

- [ ] A peer can identify inputs, commands, outputs, and failures.
- [ ] Your review distinguishes demonstrated results from future work.

## Read first

[LibreLane newcomers tutorial](https://librelane.readthedocs.io/en/stable/getting_started/newcomers/index.html): revisit run artifacts. [Tiny Tapeout documentation](https://tinytapeout.com/): inspect the current submission and hardening requirements only if you intend to integrate the block into a shuttle.

Read the named sections, not the whole manual. Write two sentences connecting the reading to this lesson's experiment before running it.

## Key ideas

A handoff needs traceability from behavior and constraints to implementation artifacts. “Final” is meaningful only relative to explicit acceptance criteria. A standalone macro exercise omits full-chip concerns such as pads, package integration, DFT, and the foundry-specific signoff contract.



## Lab

1. Choose the best feasible PWM run from Lesson 11, or document why the design remains unresolved.
2. Assemble the source commit, simulation log, resolved configuration, versions/PDK revision, experiment matrix, final netlist/GDS references, and signoff checklist.
3. Include three images from your own run: floorplan, clock or routing detail, and final layout. Add stage, run ID, layers, and interpretation to each caption.
4. Ask a peer to reproduce the run from a clean checkout. Record discrepancies and fixes in `files/handoff_template.md` copied into your evidence folder.
5. Present one tradeoff and one remaining limitation. Do not call the result tapeout-ready without the project's actual signoff review.

## Exercises

1. **Warm-up:** Name three pieces of evidence a screenshot cannot supply.
2. **Core:** Deliver a reproducible handoff and a five-minute review.
3. **Stretch:** Harden a second RTL_101 block using the same process, with its own verification and constraints.

## Hints and worked answers

<details>
<summary>Open after attempting the exercises</summary>

Tool/PDK revisions, exact constraints, and machine-readable check results are essential. A good review can conclude that a candidate is not ready; the evidence and a specific next step still represent useful engineering work.

</details>

## Checkpoint

- [ ] A peer can identify inputs, commands, outputs, and failures.
- [ ] Your review distinguishes demonstrated results from future work.

Submit the changed source/configuration, exact command, tool versions, relevant log or report excerpt, and a short explanation of the result. A screenshot supports your explanation; it does not replace the underlying report. Never submit an upstream figure as your own run.
