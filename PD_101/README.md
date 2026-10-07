# PD 101

From verified RTL to a reviewable SKY130 physical implementation with LibreLane, OpenROAD, KLayout, Magic, and Netgen.

A twelve-lesson Stone Arch Silicon track using the same course site and lesson format as [RTL_101](https://github.com/Stone-Arch-Silicon/RTL_101). Each lesson has a targeted official reading, a practical investigation, exercises with hints, and an evidence-based checkpoint. Existing manuals do the heavy lifting for installation and reference material.

Course site: https://stone-arch-silicon.github.io/PD_101/

Status: first course draft. See [VALIDATION.md](VALIDATION.md) for checks actually completed and limits. Course completion is an educational review, not fabrication signoff or a claim of exhaustive verification.

## Start here

1. Read [Lesson 1](Pages/page_1.md) and complete the upstream smoke test.
2. Clone this repository. Run `python3 scripts/run_sim.py` after activating Icarus.
3. Follow the lessons in order, keeping reports in `evidence/`.

## Tools and prerequisites

Finish RTL_101 or have equivalent sequential RTL, simulation, and synthesis knowledge. Use Linux or the upstream-supported WSL/macOS environment. Install LibreLane through its official guide; it manages the physical-design tools and PDK. Python 3 and Icarus Verilog support the local checks. Allow disk space and runtime according to the current upstream installation documentation.

## Course map

| Lesson | Topic |
|---|---|
| [1](Pages/page_1.md) | Tools and the RTL-to-GDS journey |
| [2](Pages/page_2.md) | A verified design and a reproducible baseline |
| [3](Pages/page_3.md) | Libraries, synthesis, and area |
| [4](Pages/page_4.md) | Timing constraints and honest reports |
| [5](Pages/page_5.md) | Floorplanning and utilization |
| [6](Pages/page_6.md) | Power distribution and physical-only cells |
| [7](Pages/page_7.md) | Placement, congestion, and optimization |
| [8](Pages/page_8.md) | Clock-tree synthesis and hold timing |
| [9](Pages/page_9.md) | Routing, antenna, and extraction |
| [10](Pages/page_10.md) | DRC, LVS, and a signoff evidence package |
| [11](Pages/page_11.md) | Controlled PPA experiments |
| [12](Pages/page_12.md) | Capstone: reviewable physical-design handoff |

## Repository guide

`Pages/` contains lessons; `files/labNN/` contains task sheets. Shared RTL and runnable harnesses live under `files/` and are reused across lessons. `assets/` holds original teaching diagrams. `scripts/` contains checks and analysis helpers. Solutions appear under each lesson and reference implementations are identified explicitly.

The `app.js`, `index.html`, and `style.css` framework comes from RTL_101. It already supports figure captions/credits, code highlighting, tables, and collapsible answers. Run `python3 -m http.server 8000` at the repository root to preview the site. On GitHub, configure Pages to deploy `main` from `/ (root)`.

Read [ATTRIBUTION.md](ATTRIBUTION.md) for reuse and image credits and [CONTRIBUTING.md](CONTRIBUTING.md) before contributing.

## Related tracks

- [RTL_101](https://github.com/Stone-Arch-Silicon/RTL_101)
- [PD_101](https://github.com/Stone-Arch-Silicon/PD_101)
- [verification_101](https://github.com/Stone-Arch-Silicon/verification_101)
