
import pybfms

@pybfms.bfm(hdl={
    pybfms.BfmType.Verilog : pybfms.bfm_hdl_path(__file__, "hdl/rv_addr_line_en_initiator_bfm.v"),
    pybfms.BfmType.SystemVerilog : pybfms.bfm_hdl_path(__file__, "hdl/rv_addr_line_en_initiator_bfm.v"),
    }, has_init=True)
class RvAddrLineEnInitiatorBfm():

    def __init__(self):
        self.busy = pybfms.lock()
        self.is_reset = False
        self.reset_ev = pybfms.event()
        self.adr_width = 0
        self.dat_width = 0
        self.ack_ev = pybfms.event()
        self.dat_r = 0
        pass
    
    async def write(self, adr, dat):
        await self.busy.acquire()
        
        if not self.is_reset:
            await self.reset_ev.wait()
            self.reset_ev.clear()
            
        self._access_req(adr, dat, 1)
       
        await self.ack_ev.wait()
        self.ack_ev.clear()
        
        self.busy.release()

    async def read(self, adr):
        await self.busy.acquire()
        
        if not self.is_reset:
            await self.reset_ev.wait()
            self.reset_ev.clear()
            
        self._access_req(adr, 0, 0)
       
        await self.ack_ev.wait()
        self.ack_ev.clear()
        
        self.busy.release()
        
        return self.dat_r
                
    @pybfms.import_task(pybfms.uint64_t,pybfms.uint64_t,pybfms.uint8_t)
    def _access_req(self, adr, dat_w, we):
        pass
    
    @pybfms.export_task(pybfms.uint64_t)
    def _access_ack(self, dat_r):
        self.dat_r = dat_r
        self.ack_ev.set()
        
    @pybfms.export_task(pybfms.uint32_t,pybfms.uint32_t)
    def _set_parameters(self, adr_width, dat_width):
        self.adr_width = adr_width
        self.dat_width = dat_width
        
    @pybfms.export_task()
    def _reset(self):
        self.is_reset = True
        self.reset_ev.set()
        
        
