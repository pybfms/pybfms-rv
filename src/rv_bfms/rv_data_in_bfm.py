'''
Created on Oct 7, 2019

@author: ballance
'''
import cocotb
from cocotb.drivers import Driver
from cocotb.triggers import RisingEdge, ReadOnly

@cocotb.bfm(hdl={
    cocotb.bfm_vlog : cocotb.bfm_hdl_path(__file__, "hdl/rv_data_in_bfm.v"),
    cocotb.bfm_sv : cocotb.bfm_hdl_path(__file__, "hdl/rv_data_in_bfm.v")
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