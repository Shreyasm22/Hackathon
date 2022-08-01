import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

from cocotb.triggers import Timer
import random

@cocotb.test()
async def multiplier_basic_test(dut):
    """Test for 11 * 10"""

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    A = 8
    B = 9

    # reset
    dut.C.start.value = 1
    await FallingEdge(dut.clk)
    dut.M.data_in.value = A
    await FallingEdge(dut.clk)
    dut.M.data_in.value = B

    for i in range(A+1):
        await FallingEdge(dut.clk)
    dut._log.info(f"Inp1 = {A} Inp2 = {B} Out = {int(dut.M.y.value)}")
    assert int(dut.M.y.value) == {A*B}, f"Multiplication result is incorrect: {A} * {B} != {A*B}"
           

