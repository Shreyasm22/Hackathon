# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk) 
    dut.inp_bit.value = 1
    await FallingEdge(dut.clk) 
    dut._log.info(f"Inp = {dut.inp_bit.value} State = {dut.current_state} Out = {dut.seq_seen.value}")
    assert dut.current_state.value == 0b000, "Reset is not working" 
    assert dut.seq_seen.value == 0, "Design error"

@cocotb.test()
async def test_seq_2(dut):
    
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 0
    await FallingEdge(dut.clk) 
    dut.inp_bit.value = 0
    await FallingEdge(dut.clk) 
    dut._log.info(f"Inp = {dut.inp_bit.value} State = {dut.current_state} Out = {dut.seq_seen.value}")
    assert dut.current_state.value == 0b000, "Reset is not working" 
    assert dut.seq_seen.value == 0, "Design error"



    
    