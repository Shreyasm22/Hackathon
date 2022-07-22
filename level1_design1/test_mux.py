# See LICENSE.vyoma for details
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    for i in range(0,32):
        A = '%5b'%i
        B = 0b10

        dut.sel.value = A
        dut.(inp'%d'%i).value = B


        dut._log.info(f'Sel = {(dut.sel.value)}, DUT={(dut.out.value)}')
        assert dut.inp11.value == dut.out.value, "Output is not matching"
        

