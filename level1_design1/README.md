# 31to1 Mux Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![image](https://user-images.githubusercontent.com/51830376/182038548-3813ee59-ef50-49e3-85f8-137e0ec733db.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mux module here) which takes in 5-bit selection line *sel* and 2-bit input lines *inp0-inp30* and gives 2-bit output *out*

The values are assigned to the input port using 
```
dut.sel.value = 0b01101
dut.inp13.value = 0b10

```
The assert statement is used for comparing the mux's output to the expected value.

The following error is seen:

```
assert dut.inp13.value == dut.out.value, f"Output Value mismatch. Sel = {(dut.sel.value)} Inp = {(dut.inp13.value)} Out = {(dut.out.value)}"
                     AssertionError: Output Value mismatch. Sel = 01101 Inp = 10 Out = 11
```
## Failed Scenarios

## Test Scenario1
- Test Inputs: sel=0b01100 inp12=0b11
- Expected Output: out=0b11
- Observed Output in the DUT dut.out=0b00

## Test Scenario2
- Test Inputs: sel=0b01101 inp13=0b10
- Expected Output: out=0b10
- Observed Output in the DUT dut.out=0b11

## Test Scenario3
- Test Inputs: sel=0b11110 inp30=0b10
- Expected Output: out=0b10
- Observed Output in the DUT dut.out=0b00

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
 always @(sel or inp0  or inp1 or  inp2 or inp3 or inp4 or inp5 or inp6 or
            inp7 or inp8 or inp9 or inp10 or inp11 or inp12 or inp13 or 
            inp14 or inp15 or inp16 or inp17 or inp18 or inp19 or inp20 or
            inp21 or inp22 or inp23 or inp24 or inp25 or inp26 or inp27 or 
            inp28 or inp29 or inp30 )

  begin
    case(sel)
      .
      .
      .
      5'b01101: out = inp12           ====> BUG
      5'b01101: out = inp13           ====> BUG
      .
      .
      5'b11101: out = inp29;          ====> BUG
      default: out = 0;
    endcase
  end
  
```
In the always block of mux design, the selection line 5'b01101 is assigned two input lines inp12 and inp13, selection line 5'b01100 and 5'b11110 are not defined in the design code.

## Design Fix
Failed design
![image](https://user-images.githubusercontent.com/51830376/182039144-4a2c8673-1d01-448a-b409-696fd42c728f.png)

Updating the design and re-running the test makes the test pass.
![image](https://user-images.githubusercontent.com/51830376/182039294-abbd2496-bc1b-448e-b0e8-7fdd18967c4a.png)

The updated design is checked in as mux_fix.v

