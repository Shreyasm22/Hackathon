# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    A = 0b01100

    dut.sel.value = A

    await Timer(2, units='ns')
    
    assert dut.out.value == inp12, "Adder result is incorrect: {A} != {inp12}, expected value={EXP}".format(
            A=int(dut.sel.value), inp12 =int(dut.out.value), EXP=inp12)

