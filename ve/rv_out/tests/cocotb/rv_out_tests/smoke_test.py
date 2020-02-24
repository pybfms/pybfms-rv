
from rv_bfms.rv_data_monitor_if import ReadyValidDataMonitorIF
import pybfms
import cocotb
from cocotb.triggers import Timer
import random

class SmokeTest(ReadyValidDataMonitorIF):
    
    def __init__(self):
        self.out_bfm = pybfms.find_bfm(".*u_dut")
        self.mon_bfm = pybfms.find_bfm(".*u_mon")
        self.mon_bfm.add_listener(self)
        self.recv_data_l = []
        pass
    
    def data_recv(self, d):
        self.recv_data_l.append(d)

    async def run_c(self):
        errors = 0
        
        for i in range(1,101):
            await self.out_bfm.write_c(i)
            
            # Wait briefly in between writes
            await Timer(100000*random.randint(0,10))

        # Wait briefly for a final monitor item
        await Timer(10)

        if len(self.recv_data_l) != 100:
            print("Error: too few data items received: " + str(len(self.recv_data_l)))
            errors += 1
            
        for i in range(100):
            if self.recv_data_l[i] != i+1:
                print("Incorrect data received @ " + str(i) + " (" + str(self.recv_data_l[i]))
                errors += 1


        if errors == 0:
            print("PASSED: " + cocotb.plusargs["TESTNAME"])
        else:
            print("FAILED: " + cocotb.plusargs["TESTNAME"])

@cocotb.test()
async def runtest(dut):
    await pybfms.init()
    
    test = SmokeTest()
    
    await test.run_c()
