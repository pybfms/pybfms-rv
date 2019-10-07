'''
Created on Oct 6, 2019

@author: ballance
'''
import cocotb
from cocotb.drivers import BusDriver, Driver
from cocotb.triggers import RisingEdge, ReadOnly


class DataOutReadyValidBFM(Driver):
    
    def __init__(self, clock, data, data_ready, data_valid):
        super().__init__()
        self.clock = clock
        self.data = data
        self.data_ready = data_ready
        self.data_valid = data_valid
        
        self.data.setimmediatevalue(0)
        self.data_valid.setimmediatevalue(0)

    @cocotb.coroutine
    def write(self, data):
        yield RisingEdge(self.clock)
        self.data <= data
        self.data_valid <= 1
        
        while True:
            yield RisingEdge(self.clock)
            yield ReadOnly()
            if self.data_ready:
                self.data_valid <= 0
                self.data <= 0
                break
        