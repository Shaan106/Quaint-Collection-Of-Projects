module stack #(
    parameter SIZE = 8,
    parameter DATA_WIDTH = 8)

(
    input clk,
    input rst,
    input push,
    input pop,

    input[DATA_WIDTH-1:0] data_in,

    output[DATA_WIDTH-1:0] data_out,
    
    output empty,
    output full
);

// funky and stuff for full and empty

// stack reg to hold items data
reg[DATA_WIDTH-1:0] stack_data [SIZE-1:0];

//pointer to top of stack
reg[$clog2(SIZE)-1:0] stackPointer;

assign full = (stackPointer == 3'b111);
assign empty = (stackPointer == 3'b000);

// reg to hold output value
reg[DATA_WIDTH-1:0] data_out_reg;
assign data_out = data_out_reg;

always @(posedge clk) begin

    if (rst) begin
        data_out_reg <= 8'bz;
        stackPointer <= 0;
    end
    else begin

        if (pop) begin

            if (!empty) begin
                data_out_reg <= stack_data[stackPointer - 1];
                stackPointer <= stackPointer - 1;
            end
            else begin
                data_out_reg = 8'bz;
            end

        end
        else if (push) begin
            if (!full) begin
                stack_data[stackPointer] <= data_in;
                stackPointer <= stackPointer + 1;
            end
            else begin
                data_out_reg = 8'bz;
            end
        end

    end

end

endmodule