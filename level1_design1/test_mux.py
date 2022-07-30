# See LICENSE.vyoma for details
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    mux = {0b00000 : "inp0", 0b00001 : "inp1", 0b00010 : "inp2", 0b00011 : "inp3"}

    for x in mux:
        dut.sel.value = x
        dut.mux[x].value = 0b11
        dut._log.info(f'Sel = {x} Inp = {(dut.mux[x].value)} DUT={(dut.out.value)}')
        assert dut.mux[x].value == dut.out.value, "Output is not matching"
        

