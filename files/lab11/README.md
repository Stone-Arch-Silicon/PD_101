# Lab 11: Controlled PPA experiments

[Read the lesson](../../Pages/page_11.md).

1. Use `scripts/make_variant.py` to generate configurations for utilization 30/50 and period 20/30 ns. Inspect each generated file.
2. Implement all four configurations, preserving run directories and exact tool versions.
3. Fill `files/experiment_matrix.csv` with area, setup/hold slack and corner, DRC/LVS status, and runtime. Use metrics inventory to find actual report keys rather than guessing.
4. Reject candidates that fail required checks. Select among feasible runs and explain the tradeoff. If none pass, report that outcome and the next experiment.

## Acceptance

- [ ] Four configurations and all outcomes are recorded.
- [ ] The selected candidate meets the stated acceptance criteria.
