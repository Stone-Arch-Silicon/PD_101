# TEACHING EXAMPLE ONLY. Not automatically loaded by config.json.
# Assumptions: 20 ns synchronous interface, external min/max budgets below.
create_clock -name core_clk -period 20 [get_ports clk]
set_clock_uncertainty 0.2 [get_clocks core_clk]
set_input_delay -clock core_clk -max 3 [get_ports {ui_in[*]}]
set_input_delay -clock core_clk -min 0.5 [get_ports {ui_in[*]}]
set_output_delay -clock core_clk -max 3 [get_ports {uo_out[*]}]
set_output_delay -clock core_clk -min 0.5 [get_ports {uo_out[*]}]
# Exercise: account for rst_n and unused top-level ports, loads, transitions,
# and mode assumptions. Do not use this incomplete example for signoff.
