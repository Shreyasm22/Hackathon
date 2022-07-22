# See LICENSE.vyoma for details
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux1(dut):
    """Test for mux2"""
    A = 0b00110
    B = 0b11

    dut.sel.value = A
    dut.inp11.value = B
    
    dut._log.info(type(dut.inp11))
        

