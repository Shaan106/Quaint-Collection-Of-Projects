`timescale 1ns / 1ps
module tb_mux4to1;

    reg [7:0] a, b, c, d;
    reg [1:0] select;
    wire [7:0] out;

    mux4to1 uut (
        .a(a),
        .b(b),
        .c(c),
        .d(d),
        .select(select),
        .out(out)
    );

    initial begin
        // Initialize inputs
        a = 8'hAA;  // 10101010
        b = 8'hBB;  // 10111011
        c = 8'hCC;  // 11001100
        d = 8'hDD;  // 11011101

        // Monitor output
        $monitor("Time = %0t | select = %b | out = %h", $time, select, out);

        // Test all select cases
        select = 2'b00; #10;  // Should select 'a'
        select = 2'b01; #10;  // Should select 'b'
        select = 2'b10; #10;  // Should select 'c'
        select = 2'b11; #10;  // Should select 'd'

        $finish;
    end

    initial begin
        // Dump all variable values for waveform analysis
        $dumpfile("mux4to1_tb.vcd");  // VCD file for waveform visualization
        $dumpvars(0, tb_mux4to1);     // Dump all variables from tb_mux4to1
    end

endmodule
