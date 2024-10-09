`timescale 1ns/1ps

module shift_reg_tb();


reg clk = 0;
always #5 clk = ~clk; // 10ns period

reg[3:0] D_in;
reg reset;
reg shift_dir;

wire[3:0] D_out;

shift_reg dut(.D_in(D_in),
              .reset(reset),
              .shift_dir(shift_dir),
              .clk(clk),
              .D_out(D_out));

initial begin

    $dumpfile("shift_reg_tb.vcd");
    $dumpvars(0, shift_reg_tb);

    // reset, see if in correct state
    D_in = 4'b0000;
    reset = 1'b1;
    shift_dir = 1'b0;

    #10; //wait 1 clk cycle

    $display("D_out = %b, expected 0000", D_out);

    // now set D_in to 1110
    D_in = 4'b1110; reset = 1'b0; shift_dir = 1'b0; 
    #10;
    $display("D_out = %b, expected = 1110", D_out);

    // try shifting left twice
    D_in = 4'b0000; reset = 1'b0; shift_dir = 1'b0; 
    #10;
    $display("D_out = %b, expected = 1100", D_out);
    #10;
    $display("D_out = %b, expected = 1000", D_out);

    //try shifting right twice
    D_in = 4'b0000; reset = 1'b0; shift_dir = 1'b1; 
    #10;
    $display("D_out = %b, expected = 0100", D_out);
    #10;
    $display("D_out = %b, expected = 0010", D_out);

    $finish;

end


endmodule