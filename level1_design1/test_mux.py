# See LICENSE.vyoma for details
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
   
    dut.sel.value = 0b01101
    dut.inp12.value = 0b11
    dut.inp13.value = 0b00
    await Timer(2, units='ns')
    assert dut.inp12.value == dut.out.value, "Output is not matching"
    assert dut.inp13.value == dut.out.value, "Output is not matching"






        

