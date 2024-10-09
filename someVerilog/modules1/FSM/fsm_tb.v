`timescale 1ns/1ps

module fsm_tb();

reg in;
reg reset;

reg clk = 0;
always #5 clk = ~clk; // clk period of 10ns

wire[1:0] state_out;

fsm dut(
    .in(in),
    .clk(clk),
    .reset(reset),
    .state_out(state_out)
);


initial begin
    // case 1: everything reset, should be state = 0
    in = 0;
    reset = 1;

    #10;
    $display("state_out = %b", state_out);

    // case 2: get to state 2, print everything every clock cycle
    in = 0; reset = 1; #10;
    $display("cycle 1 state_out = %b", state_out); //should be 00
    in = 1; reset = 0; #10;
    $display("cycle 2 state_out = %b", state_out); //should be 01
    in = 1; reset = 0; #10;
    $display("cycle 3 state_out = %b", state_out); //should be 10
    in = 0; reset = 0; #10;
    $display("cycle 4 state_out = %b", state_out); //should be 00


    $finish;
end



endmodule