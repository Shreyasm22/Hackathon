# See LICENSE.vyoma for details
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    for i in [0b00000, 0b00001, 0b00010, 0b00011]:
        A = i
        B = 0b11
        C = int(i)
        D = "inp" + "" + str(C) 
        dut.sel.value = A
        dut.D.value = B

        dut._log.info(f'Sel = {(dut.sel.value)}, DUT={(dut.out.value)}')
        assert dut.C.value == dut.out.value, "Output is not matching"
        

