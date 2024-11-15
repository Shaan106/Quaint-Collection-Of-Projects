module fifo #(
    parameter BUFFER_SIZE=8,
    parameter ITEM_SIZE=8)

(
    input write_en,
    input read_en,
    input rst,
    input clk,

    input[ITEM_SIZE-1:0] data_in,
    output[ITEM_SIZE-1:0] data_out
);

reg[ITEM_SIZE-1:0] buffer_data [BUFFER_SIZE-1:0];

reg[$clog2(BUFFER_SIZE)-1:0] endPointer = 0;
reg[$clog2(BUFFER_SIZE)-1:0] startPointer = 0;

reg[$clog2(BUFFER_SIZE):0] numItems = 0;

reg[ITEM_SIZE-1:0] data_out_reg;

assign data_out = read_en ? data_out_reg : 8'bz;

always @(posedge clk) begin
    
    if (rst) begin
        numItems <= 0;
        startPointer <= 0;
        endPointer <= 0;
        data_out_reg <= 8'b0;
    end
    else begin
        
        if (numItems == 0) begin
            if (write_en) begin
                buffer_data[endPointer] <= data_in;
                endPointer <= endPointer + 1;
                numItems <= numItems + 1;
            end
            data_out_reg <= 8'bz;
        end
        else if (numItems == BUFFER_SIZE) begin
            if (read_en) begin
                data_out_reg = buffer_data[startPointer];
                startPointer = startPointer + 1;
                numItems <= numItems - 1;
            end
        end
        else begin
            if (read_en) begin
                data_out_reg = buffer_data[startPointer];
                startPointer = startPointer + 1;
                numItems <= numItems - 1;
            end

            if (write_en) begin
                buffer_data[endPointer] <= data_in;
                endPointer <= endPointer + 1;
                numItems <= numItems + 1;
            end
        end

        // $display("numItems = %d, startPointer = %d, endPointer = %d", numItems, startPointer, endPointer);
        // $display("%b %b %b %b %b %b %b %b", buffer_data[0], buffer_data[1], buffer_data[2], buffer_data[3], buffer_data[4], buffer_data[5], buffer_data[6], buffer_data[7]);

    end
    
end


endmodule   