# See LICENSE.vyoma for details
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
   
dut.sel.value = 0b00000
dut.inp0.value = 0b11
assert dut.inp0.value == dut.out.value, "Output is not matching"





        

