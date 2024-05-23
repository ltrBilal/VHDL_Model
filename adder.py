from a_signal import *
from library import *
from component import *
from typing import List

class Adder(Component):

    launch = True # to write a file for this component type, just once

    def __init__(self, clock : Clock, component_name : str, first_input_signal : Signal, 
                 second_input_signal : Signal, output_signal : Signal) -> None:
        super().__init__(component_name)

        self.first_In = first_input_signal
        self.second_In = second_input_signal
        self.output = output_signal
        self.clock = clock
        self.racine = "adder"

        # list of signals
        self.signals_list : List[Signal] = []
        self.signals_list.extend([clock, self.first_In, self.second_In, self.output])

        # port
        self._Component__generate_ports(self.signals_list)
    
    # -------------------------------------------------------------------
    
    def generate_component_file(self) -> None:
        
        if self.first_In.bits >= self.second_In.bits:
            self.output.bits = self.first_In.bits + 1
        else:
            self.output.bits = self.second_In.bits + 1

        # library
        lib = Library.__new__(Library)

        # entity
        entity = f"  \nentity {self.racine} is\n"
        entity += self.port.port_to_vhdl()
        entity += f"end {self.racine};\n"

        # architecture
        arch = "\narchitecture adder_arch of adder is\n"
        arch += "begin\n"
        arch += f"      {self.output.name} <= ('0' & {self.first_In.name}) + ('0' & {self.second_In.name});\n"
        arch += "end adder_arch;"

        code = lib.library_vhdl()
        code += entity
        code += arch

        file1 = open(f'./{self.racine}.vhd', 'w')
        file1.write(code)
        
    # -------------------------------------------------------------------
        
    def component_to_vhdl(self):
        # create VHDL file for this components
        if Adder.launch == True:
            self.generate_component_file()
            Adder.launch = False
        return self._Component__generate_component_map()