from a_signal import Signal
from typing import List
from abc import ABC, abstractmethod
from port import Port
from connector import Connector

class Component(ABC):
    
    def __init__(self, component_name : str) -> None:
        self.component_name = component_name
        self.port : Port = None
        self.racine : str = None
        self.connector : Connector = None

    def __generate_ports(self, signals_list : List[Signal]):
        self.port = Port(signals_list)

    def __generate_component_map(self):
        map = f"-- instantiate an {self.racine}\n"
        map += f"   {self.component_name}: entity work.{self.racine}({self.racine}_arch)\n"
        map += "    port map(\n"
        for i, j in zip(self.signals_list, self.connector.signals_list):
            if self.signals_list[-1] == i:
                map += f"       {i.name} => {j.name}\n"
            else:
                map += f"       {i.name} => {j.name},\n"
        map += "    );\n"
        return map
    
    """
        function to generate the VHDL code file for the component
    """
    @abstractmethod
    def generate_component_file(self):
        pass

    @abstractmethod
    def component_to_vhdl(self):
        pass