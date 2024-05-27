from component import Component
from a_signal import Signal, Clock
from typing import List
from library import Library
from exception import My_Exception


class Mult(Component):

    launch = True # to write VHDL file for this component type, just once

    def __init__(self, component_name: str,clock : Clock, first_input : Signal, second_input : Signal, output : Signal) -> None:
        super().__init__(component_name)

        self.first_input = first_input
        self.second_input = second_input
        self.output = output

        self.clock = clock
        self.racine = "multiplier"
        self.path = f"./VHDL_files/{self.racine}.vhd"

        # list of signals
        self.signals_list : List[Signal] = []
        self.signals_list.extend([clock, self.first_input, self.second_input, self.output])

        # port
        self._Component__generate_ports(self.signals_list)

        try:
            number_of_bits = int(self.output.number_of_bits)
        except ValueError:
            try:
                if(self.first_input.type != self.second_input.type):
                    raise TypeError(f"ERROR : type incompatible between {self.first_input.name} and {self.second_input.name}")
            except TypeError as e:
                My_Exception.add_exception(e)
        else:
            try:
                if(number_of_bits < self.first_input.number_of_bits + self.second_input.number_of_bits):
                    raise Warning(f"WARNING : the number of bits in {output.name} is not sufficient")
            except Warning as w:
                My_Exception.add_warning(w)
        
     # -------------------------------------------------------------------
    
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
        arch += f"      {self.output.name} <= ('0' & {self.first_input.name}) * ('0' & {self.second_input.name});\n"
        arch += f"end {self.racine}_arch;"

        code = lib.library_vhdl()
        code += entity
        code += arch

        file1 = open(f'{self.path}', 'w')
        file1.write(code)
        
    # -------------------------------------------------------------------
        
    def component_to_vhdl(self):
        # create VHDL file for this components
        if Mult.launch == True:
            self.generate_component_file()
            Mult.launch = False
        return self._Component__generate_component_map()