module shift_reg(
    input[3:0] D_in,
    input shift_dir,
    input reset,
    input clk,

    output[3:0] D_out
);

reg[3:0] data;

assign D_out = data;

always @(posedge clk) begin

    if (reset)
    begin
        data <= 4'b0;
    end
    else
    begin

        if (D_in == 4'b0) 
        begin
            if (shift_dir) 
            begin
                data <= data >> 1; // >>> for arithmetic (preserving the sign)
            end
            else 
            begin
                data <= data << 1;
            end
        end
        else
        begin
            data <= D_in;
        end

    end

end

endmodule