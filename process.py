from a_signal import Signal, Clock
from typing import List, Type

class Process:
    label : str
    sensibilities : List[Signal]
    code : str

    def __init__(self, label : str, sensibilities : List[Signal], code : str = None) -> None:
        self.label = label
        self.sensibilities = sensibilities
        self.code = code

        def process_to_vhdl(self):
            pass



class Clock_Process(Process):
    
    def __init__(self, label : str, clock : Clock) -> None:
        self.label = label
        self.clock = clock
        self.sensibilities = None
    
    def process_to_vhdl(self) -> str:
        self.code = f"   {self.label} : process\n"
        self.code += "   begin\n"
        self.code += f"      {self.clock.name} <= '0';\n"
        self.code += f"      wait for {self.clock.period} {self.clock.unit};\n"
        self.code += f"      {self.clock.name} <= '1';\n"
        self.code += f"      wait for {self.clock.period} {self.clock.unit};\n"
        self.code += f"   end process;\n"
        return self.code