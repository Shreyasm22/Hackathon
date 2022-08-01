# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/Multiplier.v               # provide your design path

TOPLEVEL_2 :=    controller       # design file
TOPLEVEL_1 :=    MUL_datapath       # design file

MODULE   :=    test_multiplier    # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
