# Validation

Checked 2026-10-07.

PWM simulation PASS: cycle-by-cycle comparison, duty values 0/1/127/128/255, mid-period changes, reset, and unused I/O. Variant generator exercised at utilization 30/50 and periods 20/30 ns.

Not run here: LibreLane/SKY130 implementation, timing analysis, DRC, LVS, antenna, IR-drop analysis, and PPA sweep. The course is an implementation lab draft, not a validated physical signoff result.

Common checks: all 12 lessons present; local Markdown links, JSON, Python syntax, and JavaScript syntax pass. Both course sites were opened in Chrome and showed 12 lessons, captions, images, navigation, and code blocks. External lesson resources were checked: 36 of 37 returned HTTP 200; Arm documentation rejected the automated request with HTTP 403. Its access is not confirmed by that check.

External figures are explicitly credited upstream examples. No screenshot is represented as a successful execution of the PD labs.
