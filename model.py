from library import Library
from typing import List
from component import *
from a_signal import *

class Model:
    
    components_list : List[Component] = []
    signals_list : List[Signal] = []
    connections_list = []
    process_list = []

    def __init__(self, name : str) -> None:
        self.name = name
        self.lib = Library.__new__(Library)

    def add_component(self, component : Component):
        self.components_list.append(component)
        print("the component is added")

    def add_signal(self, signal : Signal):
        self.signals_list.append(signal)
        print("the signal is added")

    def model_to_vhdl(self):
        # add libraries
        lib = self.lib.library_vhdl()
        # entity
        entity = f"\nentity {self.name} is\n"
        # ...
        entity += "\n"
        entity += f"end {self.name};\n\n"
        # architecture
        arch = f"architecture {self.name}_arch of {self.name} is\n"
        arch += "begin\n"
        for i in self.components_list:
            arch += "\n    "
            arch += i.component_to_vhdl()
        arch += f"end {self.name}_arch;\n" 

        code = lib
        code += entity
        code += arch

        file = open("./Model.vhd", 'w')
        file.write(code)
        