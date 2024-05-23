from a_signal import Signal, Clock
from component import Component
from typing import List
from library import Library

class Registre(Component):
    launch : bool = True

    def __init__(self, clock : Clock, component_name : str, input : Signal, output : Signal) -> None:
        super().__init__(component_name)

        self.clock = clock
        self.input = input
        self.output = output
        self.racine = "registre"
        self.path = f"./VHDL_files/{self.racine}.vhd"

        self.signals_list : List[Signal] = []
        self.signals_list.extend([clock, input, output])

        self._Component__generate_ports(self.signals_list)


    def generate_component_file(self) -> None:
        # library
        lib = Library.__new__(Library)

        # entity
        entity = f"  \nentity {self.racine} is\n"
        entity += self.port.port_to_vhdl()
        entity += f"end {self.racine};\n"

        # architecture
        arch = f"\narchitecture {self.racine}_arch of {self.racine} is\n"
        arch += "begin\n"
        arch += f"      {self.output.name} <= {self.input.name};\n"
        arch += f"end {self.racine}_arch;"

        code = lib.library_vhdl()
        code += entity
        code += arch

        file1 = open(f'{self.path}', 'w')
        file1.write(code)

    # -------------------------------------------------------------------
        
    def component_to_vhdl(self):
        # create VHDL file for this components
        if Registre.launch == True:
            self.generate_component_file()
            Registre.launch = False
        return self._Component__generate_component_map()