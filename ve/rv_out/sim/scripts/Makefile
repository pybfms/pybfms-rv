#****************************************************************************
#* Makefile for rv_out
#****************************************************************************
SCRIPTS_DIR := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
include $(PACKAGES_DIR)/packages.mk
include $(PACKAGES_DIR)/simscripts/mkfiles/plusargs.mk

PLUSARGS += +tool.cocotb

PYTHONPATH:=$(SCRIPTS_DIR)/../../tests/cocotb:$(PYTHONPATH)
PYTHONPATH:=$(RV_BFMS)/src:$(PYTHONPATH)

COCOTB_BFM_MODULES += rv_bfms

TB_MODULES_HDL=rv_out_tb_hdl
VLSIM_CLOCKSPEC += clock=10ns


include $(PACKAGES_DIR)/simscripts/mkfiles/common_sim.mk
include $(PACKAGES_DIR)/packages.mk
