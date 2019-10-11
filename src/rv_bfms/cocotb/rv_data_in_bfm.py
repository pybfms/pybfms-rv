'''
Created on Oct 7, 2019

@author: ballance
'''
import cocotb
from cocotb.drivers import Driver
from cocotb.triggers import RisingEdge, ReadOnly


class ReadyValidDataInBFM(Driver):
    
    def __init__(self, bfm):
        self.bfm = bfm 
        
    @cocotb.coroutine
    def read(self):
        data = 0
        yield RisingEdge(self.clock)
        self.bfm.data_ready <= 1
        
        while True:
            yield RisingEdge(self.clock)
            yield ReadOnly()
            if self.data_valid == 1:
                yield RisingEdge(self.clock)
                self.data_ready <= 0
                data <= self.data
                break
            
        return data