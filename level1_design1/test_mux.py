# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    A = 0b01100

    dut.sel.value = A

    await Timer(2, units='ns')
    
    assert dut.out.value == INP12, "Adder result is incorrect: {A} != {INP12}, expected value={EXP}".format(
            A=int(dut.sel.value), INP12 =int(dut.out.value), EXP=INP12)

