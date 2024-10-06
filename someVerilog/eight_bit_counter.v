module up_counter_8bit (
    input clk,
    input reset,
    input enable,
    output [7:0] count_out
);

reg [7:0] counter_reg;

assign count_out = counter_reg;

always @(posedge clk) begin

    if (reset == 1) begin
        counter_reg <= 8'b0;
    end else if (enable == 1) begin
        counter_reg = counter_reg + 1;
    end 

end

endmodule
