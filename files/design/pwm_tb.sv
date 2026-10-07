`timescale 1ns/1ps
module pwm_tb;
  reg clk=0, rst_n=0;
  reg [7:0] ui_in=0;
  wire [7:0] uo_out,uio_out,uio_oe;
  integer model_count=0, model_duty=0, expected_pwm=0;
  integer high_count=0;
  always #5 clk=~clk;
  tt_um_sasi_pwm dut(.clk(clk),.rst_n(rst_n),.ena(1'b1),
    .ui_in(ui_in),.uo_out(uo_out),.uio_in(8'b0),.uio_out(uio_out),.uio_oe(uio_oe));
  task tick(input integer value,input integer reset_active);
    begin
      @(negedge clk); ui_in=value; rst_n=!reset_active;
      @(posedge clk);
      if(reset_active) begin model_count=0; model_duty=0; expected_pwm=0; end
      else begin
        expected_pwm=(model_count < model_duty);
        if(model_count==255) model_duty=value;
        model_count=(model_count+1)%256;
      end
      #1;
      if(uo_out[0] !== expected_pwm[0]) $fatal(1,"PWM mismatch");
      if(uo_out[1] !== !expected_pwm[0]) $fatal(1,"inverted output mismatch");
      if(uo_out[7:2] !== (model_count >> 2)) $fatal(1,"counter observation mismatch");
      if(uio_out !== 0 || uio_oe !== 0) $fatal(1,"unused IO mismatch");
    end
  endtask
  task check_duty(input integer value);
    begin
      tick(value,1);
      repeat(512) tick(value,0);
      high_count=0;
      repeat(256) begin tick(value,0); high_count=high_count+uo_out[0]; end
      if(high_count != value) $fatal(1,"duty %0d got %0d high cycles",value,high_count);
    end
  endtask
  initial begin
    check_duty(0); check_duty(1); check_duty(127); check_duty(128); check_duty(255);
    // A mid-period update must wait for the boundary.
    repeat(70) tick(13,0);
    repeat(300) tick(201,0);
    tick(42,1); repeat(300) tick(42,0);
    $display("PASS PWM cycle model, duty counts, update boundary, reset"); $finish;
  end
  initial begin #100000; $fatal(1,"timeout"); end
endmodule
