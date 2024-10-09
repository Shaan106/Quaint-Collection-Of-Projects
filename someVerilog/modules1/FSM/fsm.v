module fsm(
    input in,
    input clk,
    input reset,
    output[1:0] state_out
);

reg[1:0] current_state;

assign state_out = current_state;

always @(posedge clk) begin

    if (reset)
    begin
        current_state <= 2'b0;
    end
    else
    begin
        case (current_state)

            2'b00:
            begin
               if (in)
                    current_state <= 2'b01;
               else 
                    current_state <= 2'b00;
            end

            2'b01:
            begin
               if (in)
                    current_state <= 2'b10;
               else 
                    current_state <= 2'b00;
            end

            2'b10:
            begin
                current_state <= 2'b00;
            end

            default:
            begin
                current_state <= 2'b00;
            end

        endcase

    end

end 

endmodule