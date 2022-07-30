# See LICENSE.vyoma for details
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    mux = {0b00000 : 0b11, 0b00001 : 0b00, 0b00010 : 0b11, 0b00011 : 0b00}

    for x in mux:
        dut.sel.value = x
        dut.inp{int(x)}.value = mux[x]
        dut._log.info(f'Sel = {x} Inp = {mux[x]} DUT={(dut.out.value)}')
        assert dut.inp{int(x)}.value == dut.out.value, "Output is not matching"
        

