Design a **3-state FSM** using Verilog. The FSM should have the following states:
- **State 0**: On reset, the FSM should start in this state. When an input `in` is 1, move to **State 1**.
- **State 1**: If `in` is 1, move to **State 2**; if `in` is 0, go back to **State 0**.
- **State 2**: Regardless of `in`, the FSM returns to **State 0** after staying in this state for one clock cycle.

#### Requirements:
- Use an input `in`, and an input `clk` for the clock.
- There should be a reset (`rst`) signal that resets the FSM back to **State 0**.
- Use a 2-bit output `state_out` to indicate the current state.

Once you’ve written the FSM, I’ll ask you to write a testbench to verify its functionality. Let me know when you're done!