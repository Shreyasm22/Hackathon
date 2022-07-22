# See LICENSE.vyoma for details
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    for i in range(0,32):
        A = format(i, '5b')
        B = 0b11
        C = "inp" + "" + str(i)

        dut.sel.value = str(A)
        dut.C.value = B

        dut._log.info(f'Sel = {(dut.sel.value)}, DUT={(dut.out.value)}')
        assert dut.C.value == dut.out.value, "Output is not matching"
        

