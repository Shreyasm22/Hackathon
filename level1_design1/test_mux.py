# See LICENSE.vyoma for details
import os
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux1(dut):
    """Test for mux2"""

    A = 0b00000
    for i in range(0,31):
        A = A + 1;
        B = 0b11

        dut.sel.value = A
        dut.(inp + "" + i).value = B

        await Timer(2, units='ns')
    
        dut._log.info(f'Sel line = {A:05} INP12 = {B:05}  DUT={int(dut.out.value):05}')
        assert dut.out.value == B, "Sel line inp{A} doesn't exist".format(
                A=int(dut.sel.value), B =int(dut.inp10.value))

