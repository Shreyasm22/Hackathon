# 1011 Sequence Detector Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![image](https://user-images.githubusercontent.com/51830376/182038548-3813ee59-ef50-49e3-85f8-137e0ec733db.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (seq_detect_1011 module here) which takes in 1-bit input line *inp_bit* at every *negative edge* of clock and gives 1-bit output *seq_seen* at every next corresponding *positive edge* of the clock. The design gives output *seq_seen* only for 1-bit active low *reset* input.  

The values are assigned to the input port using 

```
dut.reset.value = 1
await FallingEdge(dut.clk) 
dut.reset.value = 0
dut.inp_bit.value = 0
await FallingEdge(dut.clk)
dut.inp_bit.value = 1
await FallingEdge(dut.clk)
dut.inp_bit.value = 1

```
The assert statement is used for comparing the sequence detector's output to the expected value.

The following errors are seen:

```
assert dut.current_state.value == 0b010, "State transition failed"
                     AssertionError: State transition failed
```

```
assert dut.seq_seen.value == 0, "Design error"
                     AssertionError: Design error
```


## Failed Scenarios

## Test Scenario1
- Test Inputs: reset=0, inp_bit=0,1,1
- Expected Output: seq_seen = 0, next_state = 001 
- Observed Output in the DUT dut.seq_seen=0, dut.next_state = 000

## Test Scenario2
- Test Inputs: reset=0, inp_bit=0,1,0,0,1,0,1,0
- Expected Output: seq_seen = 0, next_state = 010 
- Observed Output in the DUT dut.seq_seen=0, dut.next_state = 000

## Test Scenario3
- Test Inputs: reset=0, inp_bit=0,1,0,0,1,0,1,1,1
- Expected Output: seq_seen = 0, next_state = 001 
- Observed Output in the DUT dut.seq_seen=0, dut.next_state = 000


Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
 always @(inp_bit or current_state)
  begin
    case(current_state)
      .
      .
      SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;       ===> bug
        else
          next_state = IDLE;
      end
      .
      .
      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;       ===> bug
      
      SEQ_1011:
      begin
        next_state = IDLE;         ===> bug
      end
      
    endcase
  end
  
```
In the always state transition block of sequence detector design, there are 3 wrong state transitions in the design code.
1. When two consecutive 1's are given at input with current_state = SEQ_1, the next_state = IDLE state instead of next_state = SEQ_1.
2. When 0 is passed at input with current_state = SEQ_101, the next_state = IDLE state instead of next_state = SEQ_10.
3. When 1 is passed at input with current_state = SEQ_1011, the next_state = IDLE state instead of next_state = SEQ_1.

## Design Fix
Failed design seq_detect_1011.v

![image](https://user-images.githubusercontent.com/51830376/182148742-45b88d8e-875a-4217-982d-4ef7e2ad4acd.png)


Updating the design and re-running the test makes the test pass.

![image](https://user-images.githubusercontent.com/51830376/182150608-847ceb27-50a4-45dd-9211-6951aa35887f.png)

The updated design is checked in as seq_detect_1011_fix.v

