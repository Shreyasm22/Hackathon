# See LICENSE.vyoma for details
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    for i in range(0,32):
        B = 0b10

        dut.sel.value = i
        dut.inp{i} = B


        dut._log.info(f'Sel = {(dut.sel.value)}, DUT={(dut.out.value)}')
        assert dut.C.value == dut.out.value, "Output is not matching"
        

