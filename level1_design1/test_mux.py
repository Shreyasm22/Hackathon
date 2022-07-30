# See LICENSE.vyoma for details
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
   
   # dut.sel.value = 0b00000
    #dut.inp.value = 0b11
    #dut._log.info(f'Sel = {x} Inp = {(dut.mux[x].value)} DUT={(dut.out.value)}')
    #assert dut.mux[x].value == dut.out.value, "Output is not matching"

    dut._log.info(f'input = {(dut.inp0.value)}')



        

