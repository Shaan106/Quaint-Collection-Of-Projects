module mux4to1 (
    input [7:0] a,
    input [7:0] b,
    input [7:0] c,
    input [7:0] d,
    input [1:0] select,
    output [7:0] out
);
    // Intermediate wires to store results from lower-level muxes
    wire [7:0] top;
    wire [7:0] bottom;

    // Instantiate the first level of 2-to-1 muxes
    mux2to1 topMux (
        .a(a), 
        .b(b), 
        .select(select[0]), 
        .out(top)
    );

    mux2to1 bottomMux (
        .a(c), 
        .b(d), 
        .select(select[0]), 
        .out(bottom)
    );

    // Instantiate the second level of 2-to-1 mux to select between top and bottom
    mux2to1 outMux (
        .a(top), 
        .b(bottom), 
        .select(select[1]), 
        .out(out)
    );

endmodule


module mux2to1 (
    input [7:0] a,
    input [7:0] b,
    input select,
    output [7:0] out
);
    assign out = select ? b : a;
endmodule
