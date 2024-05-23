from library import Library
from typing import List
from component import *
from a_signal import *
from process import *
from typing import Type

class Model:
    
    components_list : List[Component] = []
    signals_list : List[Signal] = []
    connections_list : List[Connector] = []
    process_list : List[Process] = []

    def __init__(self, name : str) -> None:
        self.name = name
        self.lib = Library.__new__(Library)
        self.ports = None
        self.path = f"./VHDL_files/{self.name}.vhd"

    # -------------------------------------------------------------------

    def add_component(self, component : Component):
        if component in self.components_list:
            print(f"ERROR : component name \"{component.component_name}\" already exist")
        else:
            self.components_list.append(component)
            print(f"the component {component.component_name} is added")

    def add_signal(self, signal : Signal):
        if signal in self.signals_list:
            print(f"ERROR : signal name \"{signal.name}\" already exist")
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

    def add_process(self, process : Process):
        try:
            if process in self.process_list:
                raise ValueError(f"ERROR: process {process.label} already exist")
            else:
                if type(process) == Clock_Process:
                    for j in self.ports.signals_list:
                        if process.clock.name == j.name:
                            raise ValueError(f"ERROR : this clock \"{process.clock.name}\" can't be used for simulation (it is a port)")
            for i in self.process_list:
                if process.label == i.label:
                    raise ValueError(f"ERROR : the label {process.label} already exist")
            self.process_list.append(process)
        except ValueError as e:
            print(e)
            
    def add_port(self, ports : Port):
        self.ports = ports

    # -------------------------------------------------------------------

    def model_to_vhdl(self):
        self.__add_necessary_signals()
        # link components and connectors
        for i in self.connections_list:
            for j in self.components_list:
                if i.component.component_name == j.component_name:
                    j.connector = i
                    break
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
            if i not in self.ports.signals_list:
                i.direction = None
                arch += f"      {i.signal_to_vhdl()}; \n"
                    
        # the beginnings of architecture 
        arch += "begin\n"

        # add components
        for i in self.components_list:
            arch += "\n"
            arch += i.component_to_vhdl()

        # add process
        for i in self.process_list:
            arch += f"{i.process_to_vhdl()}\n"
        
        # the end of architecture
        arch += f"end {self.name}_arch;\n" 

        code = lib
        code += entity
        code += arch

        file = open(f"{self.path}", 'w')
        file.write(code)
        
    # -------------------------------------------------------------------
    """
        this function adds signals 
        passed in the connector or in a process if they are not in the ports session
    """
    def __add_necessary_signals(self):
        # necessary signals for connectors
        for i in self.connections_list:
            for j in i.signals_list:
                if j not in self.signals_list and j not in self.ports.signals_list:
                    self.add_signal(j)
        # necessary signals for process
        for i in self.process_list:
            if type(i) == Clock_Process and i.clock not in self.ports.signals_list:
                self.add_signal(i.clock)
            elif i.sensibilities != None:
                for j in i.sensibilities:
                    if j not in self.ports.signals_list:
                        self.add_signal(j)