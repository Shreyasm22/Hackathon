# See LICENSE.vyoma for details
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    for i in [5'b00000, 5'b00001, 5'b00010, 5'b00011]:
        A = i
        B = 0b11
        dut.sel.value = A

        dut._log.info(f'Sel = {(dut.sel.value)}, DUT={(dut.out.value)}')
        assert dut.sel.value == dut.out.value, "Output is not matching"
        

