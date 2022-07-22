# See LICENSE.vyoma for details
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux1(dut):
    """Test for mux2"""
    for i in range(0b00000, 0b11111)
        A = i
        B = 0b11

        dut.sel.value = A
        dut.inp1.value = B

        dut._log.info(f'dut._log.info(f'Sel line = {(dut.sel.value)}, DUT={(dut.out.value)}')
        assert dut.inp1.value == dut.out.value, "Output is not matching"
        

