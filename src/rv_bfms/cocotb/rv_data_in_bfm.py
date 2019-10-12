'''
Created on Oct 7, 2019

@author: ballance
'''
import cocotb
from cocotb.drivers import Driver
from cocotb.triggers import RisingEdge, ReadOnly

import bfm_core

import os


@bfm_core.bfm(bfm_hdl={
    bfm_core.HdlType.Verilog : {
        bfm_core.AbsLevel.Signal : bfm_core.hdl_path(__file__, "rv_data_in_bfm.sv")
        }
    })
class ReadyValidDataInBFM(Driver):
    
    def __init__(self, bfm):
        self.bfm = bfm 
        
    @cocotb.coroutine
    def read(self):
        data = 0
        yield RisingEdge(self.bfm.clock)
        self.bfm.data_ready <= 1
        
        while True:
            yield RisingEdge(self.bfm.clock)
            yield ReadOnly()
            if self.bfm.data_valid == 1:
                yield RisingEdge(self.bfm.clock)
                self.bfm.data_ready <= 0
                data = self.bfm.data
                break
            
        return data