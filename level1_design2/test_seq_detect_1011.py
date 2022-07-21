# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    A = 0b101100110111001101011

    dut.inp_bit.value = A

    await Timer(2, units='ns')
    
    dut._log.info(f'Inp Seq = {A:21}  DUT={(dut.seq_seen.value):21}')
    assert "Output sequence is {B}".format(
            B = (dut.seq_seen.value))
