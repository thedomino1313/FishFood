from WF_SDK import device
from WF_SDK import scope
from WF_SDK import wavegen
from WF_SDK import supplies
from WF_SDK import dmm
from WF_SDK import logic
from WF_SDK import pattern
from WF_SDK import static
from WF_SDK import protocol

from WF_SDK.protocol import i2c
from WF_SDK.protocol import spi
from WF_SDK.protocol import uart

from time import sleep


class AnalogIO:
    def __init__(self):
        self.device_data = device.open()
        
        # start the positive supply
        self.supplies_data = supplies.data()
        self.supplies_data.master_state = True
        self.supplies_data.state = True
        self.supplies_data.voltage = 3.3
        supplies.switch(self.device_data, self.supplies_data)
        
        # set all pins as output
        for index in range(4):
            static.set_mode(self.device_data, index, True)
        
    def silly(self):
        for index in range(8, 12):
            static.set_mode(self.device_data, index, False)

        for index in range(4):
            print(index, static.get_state(self.device_data, index + 8))
            self.digital_signal(index, True)
            print(index, static.get_state(self.device_data, index + 8))
    
    def probe_inputs(self, bits:list=list(range(8, 12))):
        for bit in bits:
            print(f"{bit}: {int(self.read_digital_signal(bit))}")

    def digital_signal(self, bit:int=0, state:bool=True):
        static.set_state(self.device_data, bit, state)

    def read_digital_signal(self, bit:int=8):
        return static.get_state(self.device_data, bit)

    def supply_on(self, channel:int=1, volts:int=5):
        volts = min(volts, 5)
        wavegen.generate(device_data=self.device_data, channel=channel, function=wavegen.function.dc, offset=volts)

    def disconnect(self):
        static.close(self.device_data)
        wavegen.disable(self.device_data, 1)
        wavegen.disable(self.device_data, 2)
        
        # stop and reset the power supplies
        self.supplies_data.master_state = False
        supplies.switch(self.device_data, self.supplies_data)
        supplies.close(self.device_data)
        
        # close the connection
        device.close(self.device_data)