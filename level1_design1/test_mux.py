# See LICENSE.vyoma for details
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    for i in [0b00000, 0b00001, 0b00010, 0b00011]:
        A = i

        dut.sel.value = A
        dut.inp0.value = 0b11
        dut.inp1.value = 0b11
        dut.inp2.value = 0b11
        dut.inp3.value = 0b11


        dut._log.info(f'Sel = {(dut.sel.value)}, DUT={(dut.out.value)}')
        assert dut.inp11.value == dut.out.value, "Output is not matching"
        

