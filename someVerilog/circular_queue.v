module circular_queue (
    input clk,
    input reset,
    input enqueue,
    input dequeue,
    input [7:0] data_in,
    output [7:0] data_out,
    output full,
    output empty
);

// Your implementation here

// depth 4 array of 8 bits
reg [7:0] internal_data [3:0] ;

//pointers
reg [1:0] start_pointer;
reg [1:0] end_pointer;
start_pointer <= 0;
end_pointer <= 0;

//data_out reg
reg [7:0] data_out_reg;
assign data_out = data_out_reg;

// full empty regs
reg full_reg;
reg empty_reg;
empty_reg <= 1;
full_reg <= 0;
assign empty = empty_reg;
assign full = full_reg;

// 11 - 01 = 11 + 11 = 00 

// 00 01 10 11
// 00 - 01 = 00 + 11 = 11 

always @(posedge enqueue) begin
    
    
    // check if full
    // [] [] [] []
    if (end_pointer == start_pointer - 1) begin
        full_reg <= 1;
    end else begin 
        full_reg <= 0;
        //sequential bc dont want wrong index data in
        internal_data[start_pointer] = data_in;
        start_pointer = start_pointer - 1;
    end
end

always @(posedge dequeue) begin

    //check if empty 
    if (end_pointer == start_pointer) begin
        empty_reg <= 1;
    end else begin
        empty_reg <= 0;
        //sequential again
        data_out_reg = internal_data[end_pointer];
        end_pointer = end_pointer - 1;
    end
end

always @(posedge clk) begin
    if (reset) begin
        start_pointer = 0
        end_pointer = 0
    end
end

endmodule
