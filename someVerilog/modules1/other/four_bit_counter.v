// counts up from 0 to 2^3 - 1
// synchronous reset and enable

module four_bit_counter(
    input clk,
    input reset,
    input enable,
    output[3:0] counter_out
);

reg [3:0] counter;

always @(posedge clk) begin

    if (reset) begin
        counter <= 4'b0;
    end

    if (enable) begin
        counter <= counter + 1;
    end
    

end


endmodule