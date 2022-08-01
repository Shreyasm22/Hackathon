import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def adder_basic_test(dut):
    """Test for 5 + 10"""