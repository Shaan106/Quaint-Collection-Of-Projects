module cross_correlation_valid #(
    parameter M = 8192, // Length of sequence a
    parameter N = 8192, // Length of sequence b (N ≤ M)
    parameter DATA_WIDTH = 16
)(
    input wire clk,
    input wire reset,
    input wire valid_in_A,
    input wire valid_in_B,
    input wire signed [DATA_WIDTH-1:0] a_in,
    input wire signed [DATA_WIDTH-1:0] b_in,
    output reg valid_out,
    output reg signed [2*DATA_WIDTH-1:0] correlation_out
);

    // Calculate output length
    localparam OUTPUT_LEN = M - N + 1;

    // Internal memories to store the input sequences
    reg signed [DATA_WIDTH-1:0] a_mem [0:M-1];
    reg signed [DATA_WIDTH-1:0] b_mem [0:N-1];

    // Control variables
    integer i, k;
    reg signed [2*DATA_WIDTH-1:0] sum;

    // Define state constants
    localparam [2:0]
        IDLE    = 3'd0,
        LOAD_A  = 3'd1,
        LOAD_B  = 3'd2,
        COMPUTE = 3'd3,
        OUTPUT  = 3'd4;

    // Declare the state register
    reg [2:0] state;

    initial begin
        state = IDLE;
        valid_out = 0;
        correlation_out = 0;
        sum = 0;
        i = 0;
        k = 0;
    end

    // State machine implementation
    always @(posedge clk or posedge reset) begin
        if (reset) begin
            $display("reset flag");
            state <= IDLE;
            valid_out <= 0;
            correlation_out <= 0;
            sum <= 0;
            i <= 0;
            k <= 0;
        end else begin
            // $display("start");
            case (state)
                IDLE: begin
                    $display("valid_in = %b", valid_in_A);
                    $display("idle flag");
                    if (valid_in_A) begin
                        state <= LOAD_A;
                        i <= 0;
                    end
                end
                LOAD_A: begin
                    $display("load_a flag");
                    $display("valid_in = %b", valid_in_A);
                    $display("i = %d", i);
                    if (valid_in_A) begin
                        a_mem[i] <= a_in;
                        i <= i + 1;
                        if (i == M - 1) begin
                            state <= LOAD_B;
                            i <= 0;
                        end
                    end
                end
                LOAD_B: begin
                    // $display("load_b flag, i = %d", i);
                    if (valid_in_B) begin
                        b_mem[i] <= b_in;
                        i <= i + 1;
                        if (i == N - 1) begin
                            state <= COMPUTE;
                            i <= 0;
                            k <= 0;
                            sum <= 0;
                        end
                    end
                end
                COMPUTE: begin
                    $display("compute flag");
                    if (i < N) begin
                        sum <= sum + a_mem[i + k] * b_mem[i];
                        i <= i + 1;
                    end else begin
                        i <= 0;
                        correlation_out <= sum;
                        valid_out <= 1;
                        sum <= 0;
                        k <= k + 1;
                        if (k < OUTPUT_LEN) begin
                            // Prepare for next computation
                            state <= COMPUTE;
                            valid_out <= 0;
                        end else begin
                            state <= OUTPUT;
                        end
                    end
                end
                OUTPUT: begin
                    $display("output flag");
                    // Hold the last valid output
                    valid_out <= 0;
                    // Optionally, you can reset or wait for the next computation
                    // state <= IDLE;
                end
                default: begin
                    state <= IDLE; // Default state
                end
            endcase
        end
    end

endmodule
