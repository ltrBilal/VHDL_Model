from library import Library
from typing import List
from component import *
from a_signal import *
from connector import *

class Model:
    
    components_list : List[Component] = []
    signals_list : List[Signal] = []
    connections_list : List[Connector] = []
    process_list = []

    def __init__(self, name : str) -> None:
        self.name = name
        self.lib = Library.__new__(Library)
        self.ports = None

    # -------------------------------------------------------------------

    def add_component(self, component : Component):
        if component in self.components_list:
            print(f"ERROR : component name \"{component.component_name}\" already existe")
        else:
            self.components_list.append(component)
            print(f"the component {component.component_name} is added")

    def add_signal(self, signal : Signal):
        if signal in self.signals_list:
            print(f"ERROR : signal name \"{signal.name}\" already existe")
        else:
            self.signals_list.append(signal)
            print(f"the signal {signal.name} is added")

    def add_connector(self, connector : Connector):
        if connector.component in self.connections_list:
            print(f"ERROR : the component \"{connector.component.component_name}\" has already a connector")
        else:
            self.connections_list.append(connector)
            connector.component.connector = connector
            print(f"the connector for {connector.component.component_name} is added")

    def add_port(self, ports : Port):
        self.ports = ports

    # -------------------------------------------------------------------

    def model_to_vhdl(self):
        # add connector
        self.__connect()
        # add libraries
        lib = self.lib.library_vhdl()
        # entity
        entity = f"\nentity {self.name} is\n"
        if self.ports != None:
            entity += self.ports.port_to_vhdl()
        entity += f"end {self.name};\n\n"
        # architecture
        arch = f"architecture {self.name}_arch of {self.name} is\n"

        # add signals
        signals_list_copy = [s.copy() for s in self.signals_list] # make a copy of all signals in original list
        for i in signals_list_copy:
            i.direction = None
            arch += f"      {i.signal_to_vhdl()}; \n"
        arch += "begin\n"

        # add components
        for i in self.components_list:
            arch += "\n"
            arch += i.component_to_vhdl()
        
        arch += f"end {self.name}_arch;\n" 

        code = lib
        code += entity
        code += arch

        file = open(f"./{self.name}.vhd", 'w')
        file.write(code)
        

    def __connect(self):
        for i in self.connections_list:
            for j in i.signals_list:
                if j not in self.signals_list and j not in self.ports.signals_list:
                    self.add_signal(j)