`timescale 1ns / 1ps

module dff_tb();

    reg d;
    reg reset;
    reg clk = 0;
    
    wire q;

    dff dut(.d(d), 
            .reset(reset),
            .clk(clk),
            .q(q));

    // 10ns clk period
    always #5 clk = ~clk;

    parameter TEST_DATA_SIZE = 4;

    reg[1:0] test_inputs [TEST_DATA_SIZE - 1:0]; //4 test data items of form {d, reset}

    //for the for loop
    integer i;
    integer j;

    initial begin
        
        for (i = 0; i < TEST_DATA_SIZE; i++) begin
            test_inputs[i] = i;
        end

        // Dump signals to VCD file
        $dumpfile("dff_tb.vcd");    // Name of the VCD file
        $dumpvars(0, dff_tb);             // Dump everything in the current testbench hierarchy

        //start testing
        // #20;

        for (j = 0; j < TEST_DATA_SIZE; j++) begin 
            d = test_inputs[j][0];
            reset = test_inputs[j][1];
            #10;
            // $display("clk = %b", clk);
            #10;
            // $display("clk = %b", clk);
            // $display("clk = %b", clk);
            $display("d = %b, reset = %b, q = %b", d, reset, q);
        end

        $finish;

    end

endmodule