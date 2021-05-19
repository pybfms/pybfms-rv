'''
Created on Oct 7, 2019

@author: ballance
'''
import pybfms

@pybfms.bfm(hdl={
    pybfms.BfmType.Verilog : pybfms.bfm_hdl_path(__file__, "hdl/rv_data_in_bfm.v"),
    pybfms.BfmType.SystemVerilog : pybfms.bfm_hdl_path(__file__, "hdl/rv_data_in_bfm.v"),
    }, has_init=True)
class ReadyValidDataInBFM():
    
    def __init__(self):
        self.data_width = 0
        self.recv_cb = []
        self.have_reset = False
        self.reset_ev = pybfms.event()
        
    def add_recv_cb(self, cb):
        self.recv_cb.append(cb)
        
    def del_recv_cb(self, cb):
        self.recv_cb.remove(cb)
        
    async def wait_reset(self):
        if not self.have_reset:
            await self.reset_ev.wait()
        
    async def recv(self):
        ev = pybms.event()        
        def cb(data):
            nonlocal ev
            ev.set(data)
            
        self.add_recv_cb(cb)
        await ev.wait()
        self.del_recv_cb(cb)
        
        return ev.data

    @pybfms.export_task(pybfms.uint8_t)
    def _set_parameters(self, data_width):
        self.data_width = data_width
        
    @pybfms.export_task(pybfms.uint64_t)
    def _recv(self, data):
        if len(self.recv_cb) > 0:
            for cb in self.recv_cb.copy():
                cb(data)
                
    @pybfms.export_task()
    def _reset(self):
        self.have_reset = True
        self.reset_ev.set()
