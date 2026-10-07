from pathlib import Path
import subprocess
root=Path(__file__).resolve().parents[1]
build=root/'sim_build'; build.mkdir(exist_ok=True)
subprocess.run(['iverilog','-g2012','-s','pwm_tb','-o',str(build/'pwm.vvp'),str(root/'files/design/project.v'),str(root/'files/design/pwm_tb.sv')],check=True)
subprocess.run(['vvp',str(build/'pwm.vvp')],check=True,cwd=root)
