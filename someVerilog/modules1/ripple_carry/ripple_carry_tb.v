`timescale 1ns/1ps

module ripple_carry_tb();

reg[3:0] A, B;

reg C_in;

wire[3:0] S;
wire C_out;

ripple_carry dut(
    .A(A),
    .B(B),
    .C_in(C_in),
    .S(S),
    .C_out(C_out)
);

integer i;

initial begin
    // set all inputs initially to 0
    A = 4'b0;
    B = 4'b0;
    C_in = 1'b0;

    // go through some combinations of inputs
    for (i = 0; i < 8; i++) begin
        A = i;
        B = i + 4;
        C_in = i % 2;
        #10;
        $display("A = %d, B = %d, C = %d,   S = %d, C_out = %d", A, B, C_in, S, C_out);
    end

    $finish;

end


endmodule