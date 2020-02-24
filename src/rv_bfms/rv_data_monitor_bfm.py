'''
Created on Oct 6, 2019

@author: ballance
'''

import pybfms

@pybfms.bfm(hdl={
    pybfms.BfmType.Verilog : pybfms.bfm_hdl_path(__file__, "hdl/rv_data_monitor_bfm.v"),
    pybfms.BfmType.SystemVerilog : pybfms.bfm_hdl_path(__file__, "hdl/rv_data_monitor_bfm.v")
    }, has_init=True)
class ReadyValidDataMonitorBFM():

    def __init__(self):
        self.listener_l = []
        self.data_width = 0
        
    
    def add_listener(self, l):
        self.listener_l.append(l)

    @pybfms.export_task(pybfms.uint64_t)
    def _data_recv(self, d):
        for l in self.listener_l:
            l.data_recv(d)

    @pybfms.export_task(pybfms.uint64_t)            
    def _set_parameters(self, data_width):
        self.data_width = data_width
    
