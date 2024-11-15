`timescale 1ns/1ps

module fifo_tb();

reg write_en;
reg read_en;
reg rst;
reg clk = 0;

// 10 ns clock period
always #5 clk = !clk;

reg[7:0] data_in;
wire[7:0] data_out;


fifo #(.BUFFER_SIZE(8), .ITEM_SIZE(8)) dut (
    .write_en(write_en),
    .read_en(read_en),
    .rst(rst),
    .clk(clk),
    .data_in(data_in),
    .data_out(data_out)
);


initial begin
    // set initial inputs, reset = 1
    write_en = 1'b0;
    read_en = 1'b0;
    rst = 1'b1;
    data_in = 8'b0;

    $dumpfile("fifo_dump.vcd");
    $dumpvars(0, fifo_tb);

    #10;

    $display("data_out = %b, expected = 00000000", data_out);

    // push 2 items in, then pop and read
    write_en = 1'b1;
    read_en = 1'b0;
    rst = 1'b0;
    data_in = 1;
    #10;
    data_in = 3;
    #10;
    data_in = 7;
    #10;
    data_in = 15;
    #10;
    data_in = 31; 
    #10;
    data_in = 63; 
    #10;
    data_in = 127; 
    #10;
    data_in = 255; 
    #10;
    data_in = 17; // I should never read this out 
    #10;
    data_in = 21; // I should never read this out 
    #10;

    //get data out
    write_en = 1'b0;
    read_en = 1'b1;
    rst = 1'b0;
    #10;
    $display("data_out = %b, expected = 1", data_out);
    #10;
    $display("data_out = %b, expected = 3", data_out);
    #10;
    $display("data_out = %b, expected = 7", data_out);
    #10;
    $display("data_out = %b, expected = 15", data_out);
    #10;
    $display("data_out = %b, expected = 31", data_out);
    #10;
    $display("data_out = %b, expected = 63", data_out);
    #10;
    $display("data_out = %b, expected = 127", data_out);
    #10;
    $display("data_out = %b, expected = 255", data_out);
    #10;
    $display("data_out = %b, expected = 17 -> should not read out", data_out); //should not read out

    $finish;
end


endmodule