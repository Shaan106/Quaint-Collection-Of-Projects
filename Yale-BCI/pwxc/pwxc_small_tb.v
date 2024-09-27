`timescale 1ns / 1ps

module cross_correlation_valid_tb;

    // Parameters
    parameter M = 3; // Length of sequence a
    parameter N = 3; // Length of sequence b
    parameter DATA_WIDTH = 16;

    // Signals
    reg clk;
    reg reset;
    reg valid_in_A;
    reg valid_in_B;
    reg signed [DATA_WIDTH-1:0] a_in;
    reg signed [DATA_WIDTH-1:0] b_in;
    wire valid_out;
    wire signed [2*DATA_WIDTH-1:0] correlation_out;

    // Instantiate the cross_correlation_valid module
    cross_correlation_valid #(
        .M(M),
        .N(N),
        .DATA_WIDTH(DATA_WIDTH)
    ) uut (
        .clk(clk),
        .reset(reset),
        .valid_in_A(valid_in_A),
        .valid_in_B(valid_in_B),
        .a_in(a_in),
        .b_in(b_in),
        .valid_out(valid_out),
        .correlation_out(correlation_out)
    );

    // Clock generation
    always #5 clk = ~clk; // 100 MHz clock

    // Test sequences
    reg signed [DATA_WIDTH-1:0] a_seq [0:M-1];
    reg signed [DATA_WIDTH-1:0] b_seq [0:N-1];

    integer i;

    initial begin
        // Initialize signals
        clk = 0;
        reset = 1;
        valid_in_A = 0;
        valid_in_B = 0;
        a_in = 0;
        b_in = 0;

        // Initialize test sequences
        a_seq[0] = 1;
        a_seq[1] = 2;
        a_seq[2] = 3;

        b_seq[0] = 1;
        b_seq[1] = 2;
        b_seq[2] = 4;

        // Apply reset
        #10;
        reset = 0;

        // Wait for a few clock cycles
        #10;

        // Start loading sequence a
        valid_in_A = 1;
        for (i = 0; i < M; i = i + 1) begin
            a_in = a_seq[i];
            b_in = 0; // b_in is ignored during loading of a_seq
            #10;
        end

        // Start loading sequence b
        valid_in_B = 1;
        for (i = 0; i < N; i = i + 1) begin
            a_in = 0; // a_in is ignored during loading of b_seq
            b_in = b_seq[i];
            #10;
        end

        // Stop valid_in after loading
        valid_in_A = 0;
        valid_in_B = 0;
        a_in = 0;
        b_in = 0;

        // Wait for computation to complete
        wait (valid_out == 1);
        #10;

        // Display the result
        $display("Correlation result: %d", correlation_out);
        if (correlation_out == 17) begin
            $display("Test PASSED.");
        end else begin
            $display("Test FAILED.");
        end

        // Finish simulation
        $stop;
    end

endmodule
