module ripple_carry(
    input[3:0] A,
    input[3:0] B,
    input C_in,

    output[3:0] S,
    output C_out
);

    wire c0,c1,c2,c3;

    full_adder fa0(.a(A[0]),
                   .b(B[0]),
                   .c_in(C_in),
                   .s(S[0]),
                   .c_out(c0));

    full_adder fa1(.a(A[1]),
                   .b(B[1]),
                   .c_in(c0),
                   .s(S[1]),
                   .c_out(c1));

    full_adder fa2(.a(A[2]),
                   .b(B[2]),
                   .c_in(c1),
                   .s(S[2]),
                   .c_out(c2));

    full_adder fa3(.a(A[3]),
                   .b(B[3]),
                   .c_in(c2),
                   .s(S[3]),
                   .c_out(C_out));

endmodule

module full_adder(
    input a,
    input b,
    input c_in,

    output s,
    output c_out
);

assign s = (a ^ b) ^ c_in;
assign c_out = (a & b) | ((a ^ b) & c_in);

endmodule