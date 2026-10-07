# Lab 05: Floorplanning and utilization

[Read the lesson](../../Pages/page_5.md).

1. Open a floorplan-stage ODB/DEF from the baseline using the documented GUI flow. Identify die, core, cell rows, and pins.
2. Run `python3 scripts/make_variant.py --util 30 --period 20` and inspect the generated JSON beside the baseline configuration.
3. Implement the printed variant configuration with LibreLane. Repeat at utilization 50, keeping the same clock target.
4. Compare core area, placement density, routed wire length (if reported), and DRC outcomes. Save both run IDs.

## Acceptance

- [ ] You saved two controlled utilization experiments.
- [ ] Your comparison separates die/core/cell area.
