'''
Created on Oct 7, 2019

@author: ballance
'''
import pybfms

@pybfms.bfm(hdl={
    pybfms.BfmType.Verilog : pybfms.bfm_hdl_path(__file__, "hdl/rv_data_in_bfm.v"),
    pybfms.BfmType.SystemVerilog : pybfms.bfm_hdl_path(__file__, "hdl/rv_data_in_bfm.v")
    })
class ReadyValidDataInBFM():
    
    def __init__(self):
        self.data_width = 0
        self.impl = None

    def set_impl(self, impl):
        self.impl = impl
                
#     @cocotb.coroutine
#     def read(self):
#         data = 0
#         yield RisingEdge(self.bfm.clock)
#         self.bfm.data_ready <= 1
#         
#         while True:
#             yield RisingEdge(self.bfm.clock)
#             yield ReadOnly()
#             if self.bfm.data_valid == 1:
#                 yield RisingEdge(self.bfm.clock)
#                 self.bfm.data_ready <= 0
#                 data = self.bfm.data
#                 break
#             
#         return data