import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

from cocotb.triggers import Timer
import random

@cocotb.test()
async def adder_basic_test(dut):
    """Test for 5 + 10"""

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    A = 11
    B = 10

    # reset
    dut.start.value = 1
    await FallingEdge(dut.clk)
    dut.data_in.value = A
    await FallingEdge(dut.clk)
    dut.data_in.value = B

    dut._log.info(f"Inp1 = {A} Inp2 = {B} Out = {dut.y.value}")
    assert dut.y.value == A*B, f"Multiplication result is incorrect: {A} * {B} != {A*B}"
           

