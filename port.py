from a_signal import Signal
from typing import List

class Port:

    def __init__(self, signals_list : List[Signal]) -> None:
        self.signals_list = signals_list

    
    def port_to_vhdl(self):
        port = "   port(\n"
        for i in self.signals_list:
            if self.signals_list[-1] == i:
                port += f"          {i.signal_to_vhdl()}\n"
            else:
                port += f"          {i.signal_to_vhdl()};\n"
        port += "   );\n"
        return port