# Contributing

Keep `Pages/page_N.md` sequential. Use `Pages/TEMPLATE.md` for new lessons. Define the objective, a short reading assignment, a command or concrete investigation, warm-up/core/stretch exercises, hints or solutions, and evidence required for completion. Use the existing site renderer.

Prefer links to the tool author's documentation over rewriting an installation manual. Record tested tool versions. Images need meaningful alt text, captions, and a source/license; label conceptual diagrams and upstream example screenshots honestly. Never invent a successful tool report.

Run `python3 scripts/check_course.py` from the repository root. Run the relevant simulation before changing RTL or its checkers. Physical implementation changes also need a new LibreLane run with the tool/PDK revisions and signoff report references recorded. Update `VALIDATION.md` with what was actually run.
