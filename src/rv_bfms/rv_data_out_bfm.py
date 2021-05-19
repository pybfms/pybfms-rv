'''
Created on Oct 6, 2019

@author: ballance
'''

import pybfms


@pybfms.bfm(hdl={
    pybfms.BfmType.Verilog : pybfms.bfm_hdl_path(__file__, "hdl/rv_data_out_bfm.v"),
    pybfms.BfmType.SystemVerilog : pybfms.bfm_hdl_path(__file__, "hdl/rv_data_out_bfm.v")
    }, has_init=True)
class ReadyValidDataOutBFM():

    def __init__(self):
        self.busy = pybfms.lock()
        self.ack_ev = pybfms.event()
        self.data_width = 0

    async def send(self, data):
        '''
        Writes the specified data word to the interface
        '''
        
        await self.busy.acquire()
        self._send_req(data)

        # Wait for acknowledge of the transfer
        await self.ack_ev.wait()
        self.ack_ev.clear()

        self.busy.release()

    @pybfms.import_task(pybfms.uint64_t)
    def _send_req(self, d):
        pass
    
    @pybfms.export_task()
    def _send_ack(self):
        self.ack_ev.set()
        
    @pybfms.export_task(pybfms.uint32_t)
    def _set_parameters(self, data_width):
        self.data_width = data_width
    
