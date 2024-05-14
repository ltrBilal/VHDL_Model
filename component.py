from a_signal import Signal
from typing import List
from abc import ABC, abstractmethod

class Component(ABC):
    
    def __init__(self, component_name : str) -> None:
        self.component_name = component_name
        self.port = None
        self.racine = None

    def __generate_ports(self, signals_list : List[Signal]):
        self.port = "   port(\n"
        for i in signals_list:
            if signals_list[-1] == i:
                self.port += f"          {i.signal_to_vhdl()}\n"
            else:
                self.port += f"          {i.signal_to_vhdl()};\n"
        self.port += "   );\n"

    def __generate_component_map(self):
        map = f"-- instanciation for {self.racine}\n"
        map += f"   {self.component_name}: entity work.{self.racine}({self.racine}_arch)\n"
        map += "    port map(\n"
        for i in self.signals_list:
            if self.signals_list[-1] == i:
                map += f"       {i.name} => {i.name}\n"
            else:
                map += f"       {i.name} => {i.name},\n"
        map += "    );\n"
        return map
    
    """
        function to generate the VHDL code file for the component
    """
    @abstractmethod
    def generate_component_file(self):
        pass

    @abstractmethod
    def generate_component_body(self, name):
        pass