`timescale 1ns/1ps

module stack_tb();

    reg clk = 0;

    always #5 clk = ~clk;

    reg rst;
    reg push;
    reg pop;

    reg[8-1:0] data_in;

    wire[8-1:0] data_out;
    
    wire empty;
    wire full;

    stack dut(
        .clk(clk),
        .rst(rst),
        .push(push),
        .pop(pop),
        .data_in(data_in),
        .data_out(data_out),
        .empty(empty),
        .full(full)
    );

    initial begin
        // set initial inputs, reset all
        rst = 1'b1;
        push = 1'b0;
        pop = 1'b0;
        #10; // 1 clock cycle
        
        // see outputs
        $display("data_out = %b, full = %b, empty = %b", data_out, full, empty);

        // try push and pop
        rst = 1'b0;
        push = 1'b1;
        data_in = 8'b00000011;
        #10;
        $display("data_out = %b, full = %b, empty = %b", data_out, full, empty);
        push = 1'b0;
        pop = 1'b1;
        #10;
        $display("data_out = %b, full = %b, empty = %b", data_out, full, empty);

        $display("EDGE CASE: \n");

        // edge case add 10 items
        rst = 1'b1;
        push = 1'b0;
        pop = 1'b0;
        #10;
        rst = 1'b0;
        push = 1'b1;
        data_in = 8'b1;
        #10;
        data_in = 8'd2;
        #10;
        data_in = 3;
        #10;
        data_in = 4;
        #10;
        data_in = 5;
        #10;
        data_in = 6;
        #10;
        data_in = 7;
        #10;
        data_in = 8;
        #10;
        data_in = 9; //shouldn't be popped
        #10;
        data_in = 10; //shouldn't be popped
        #10;

        //pop 10 items! (last 2 should not)
        pop = 1'b1;
        push = 1'b0;
        #10;
        $display("data_out = %b, full = %b, empty = %b", data_out, full, empty);
        #10;
        $display("data_out = %b, full = %b, empty = %b", data_out, full, empty);
        #10;
        $display("data_out = %b, full = %b, empty = %b", data_out, full, empty);
        #10;
        $display("data_out = %b, full = %b, empty = %b", data_out, full, empty);
        #10;
        $display("data_out = %b, full = %b, empty = %b", data_out, full, empty);
        #10;
        $display("data_out = %b, full = %b, empty = %b", data_out, full, empty);
        #10;
        $display("data_out = %b, full = %b, empty = %b", data_out, full, empty);
        #10;
        $display("data_out = %b, full = %b, empty = %b", data_out, full, empty);
        #10;
        $display("data_out = %b, full = %b, empty = %b", data_out, full, empty);
        #10;
        $display("data_out = %b, full = %b, empty = %b", data_out, full, empty);


        $finish;

    end



endmodule