'''
Created on Oct 6, 2019

@author: ballance
'''
import cocotb
from cocotb.drivers import Driver
from cocotb.triggers import RisingEdge, ReadOnly
import os

import bfm_core
from bfm_core import HdlType, AbsLevel


@bfm_core.bfm(bfm_hdl={
    HdlType.Verilog : {
            AbsLevel.Signal : bfm_core.hdl_path(__file__, "rv_data_out_bfm.sv")
        }
    })
class ReadyValidDataOutBFM(Driver):
    
    def __init__(self, bfm):
        super().__init__()
        self.clock = bfm.clock
        self.data = bfm.data
        self.data_ready = bfm.data_ready
        self.data_valid = bfm.data_valid
        
        self.data.setimmediatevalue(0)
        self.data_valid.setimmediatevalue(0)
        self.posedge = RisingEdge(self.clock)

    @cocotb.coroutine
    def write(self, data):
        '''
        Writes the specified data word to 
        '''
        
        yield RisingEdge(self.clock)
        self.data <= data
        self.data_valid <= 1
        
        while True:
            yield RisingEdge(self.clock)
            yield ReadOnly()
            if self.data_ready == 1:
                yield RisingEdge(self.clock)
                self.data_valid <= 0
                self.data <= 0
                break
        