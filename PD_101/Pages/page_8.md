# Lesson 8: Clock-tree synthesis and hold timing

Inspect the real clock network and understand why timing changes after it is built.

> [!NOTE]
> Before you start: Complete [Lesson 7](page_7.md). Allow 90–150 minutes, plus tool runtime. Keep your work in `evidence/lesson08/`. Lab notes: [files/lab08](../files/lab08/).

## What you will learn

- [ ] You identified the clock tree and report assumptions.
- [ ] You explained one setup/hold change after CTS.

## Read first

[OpenROAD clock-tree synthesis](https://openroad.readthedocs.io/en/latest/main/src/cts/README.html): read the overview and clock-tree reporting commands. Review the timing path terminology from Lesson 4.

Read the named sections, not the whole manual. Write two sentences connecting the reading to this lesson's experiment before running it.

## Key ideas

Before clock-tree synthesis (CTS), the analysis may use an ideal clock. After CTS, clock buffers and wire delays produce insertion delay and skew between sinks. Skew can help one setup relationship while hurting hold. The clock network consumes area and routing resources even though it was not explicit in the RTL.



## Lab

1. Find the CTS stage and clock reports in the baseline run. Record clock root, sink count, inserted buffers, and reported skew when available.
2. Display the clock tree separately from signal wiring in OpenROAD.
3. Compare setup and hold reports before and after CTS using the same corner where possible.
4. Choose one path and explain which terms changed. Record whether the report uses ideal or propagated clocks.

## Exercises

1. **Warm-up:** Define insertion delay and skew without treating them as synonyms.
2. **Core:** Why can a new clock buffer affect hold slack?
3. **Stretch:** Draw a launch/capture timing sketch with a late capture clock and explain the setup and hold implications for the same-edge hold relationship.

## Hints and worked answers

<details>
<summary>Open after attempting the exercises</summary>

Insertion delay is source-to-sink latency. Skew is a difference between sink arrival times. A later capture clock gives a setup path more time for the next edge but can increase the same-edge hold requirement. Always check the actual launch/capture edge relationship in the report.

</details>

## Checkpoint

- [ ] You identified the clock tree and report assumptions.
- [ ] You explained one setup/hold change after CTS.

Submit the changed source/configuration, exact command, tool versions, relevant log or report excerpt, and a short explanation of the result. A screenshot supports your explanation; it does not replace the underlying report. Never submit an upstream figure as your own run.
