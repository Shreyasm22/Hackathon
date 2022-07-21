# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux1(dut):
    """Test for mux2"""
    for i in range(0,31):
        A = '{0:05b}'.format(i)
        B = 0b11

        dut.sel.value = '{0:05b}'.format(i)
        dut.inp1.value = B

        await Timer(2, units='ns')
    
        dut._log.info(f'Sel line = {A:05} INP12 = {B:05}  DUT={int(dut.out.value):05}')
        assert dut.out.value == B, "Sel line inp{A} doesn't exist".format(
                A=int(dut.sel.value), B =int(dut.inp1.value))

