module dff (
    input d,
    input reset,
    input clk,

    output q
);

reg data;

assign q = data;

always @(posedge clk) begin
    
    if (reset)
    begin
        data <= 1'b0;
    end
    else 
    begin
        data <= d;
    end

end

endmodule