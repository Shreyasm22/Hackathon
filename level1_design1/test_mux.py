# See LICENSE.vyoma for details
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    for i in range(0,32):
        A = f'%5b%i'
        B = 0b11

        dut.sel.value = A
        dut.inp{int(i)}.value = B

        dut._log.info(f'dut._log.info(f'Sel line = {(dut.sel.value)}, DUT={(dut.out.value)}')
        assert dut.inp{int(i)}.value == dut.out.value, "Output is not matching"
        

