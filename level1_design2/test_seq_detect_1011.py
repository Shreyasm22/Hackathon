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


    dut.inp_bit.value = 1
    dut.inp_bit.value = 0
    dut.inp_bit.value = 1
    dut.inp_bit.value = 1

    dut._log.info(f'Inp Seq = {A:04}  DUT={bin(dut.seq_seen.value)}')
    assert "Output sequence is {B}".format(
            B = (dut.seq_seen.value))
