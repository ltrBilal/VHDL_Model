from a_signal import Signal, Clock
from typing import List, Type

class Process:
    label : str
    sensibilities : List[Signal]
    code : str

    def __init__(self, label : str, sensibilities : List[Signal] = None, code : str = None) -> None:
        self.label = label
        self.sensibilities = sensibilities
        self.code = code

    def process_to_vhdl(self) -> str:
        seq = f"    -- {self.label} process\n"
        if self.sensibilities == None:
            seq += f"   {self.label} : process\n"
        else:
            seq += f"   {self.label} : process ("
            for i in self.sensibilities:
                if self.sensibilities[-1] == i:
                    seq += f"{i.name})\n"
                else:
                    seq += f"{i.name},"
        seq += "   begin\n"
        seq += f"       {self.code}\n"
        seq += f"   end process;\n"
        return seq


class Clock_Process(Process):
    
    def __init__(self, label : str, clock : Clock) -> None:
        self.label = label
        self.clock = clock
        self.sensibilities = None
    
    def process_to_vhdl(self) -> str:
        self.code = "   -- clock simulation\n"
        self.code += f"   {self.label} : process\n"
        self.code += "   begin\n"
        self.code += f"      {self.clock.name} <= '0';\n"
        self.code += f"      wait for {self.clock.period} {self.clock.unit};\n"
        self.code += f"      {self.clock.name} <= '1';\n"
        self.code += f"      wait for {self.clock.period} {self.clock.unit};\n"
        self.code += f"   end process;\n"
        return self.code