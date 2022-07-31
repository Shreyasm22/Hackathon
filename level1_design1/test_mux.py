# See LICENSE.vyoma for details
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux1(dut):
    """Test for mux2"""
   
    dut.sel.value = 0b01101
    dut.inp13.value = 0b11
    await Timer(2, units='ns')
    assert dut.inp12.value == dut.out.value, "Output is not matching"

@cocotb.test()
async def test_mux2(dut):
    
    dut.sel.value = 0b01000
    dut.inp8.value = 0b10
    await Timer(2, units='ns')
    assert dut.inp8.value == dut.out.value, "Output is not matching"

    






        

