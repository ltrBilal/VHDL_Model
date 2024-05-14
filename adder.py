from a_signal import *
from library import *
from component import *
from typing import List

class Adder(Component):

    launch = True # to write a file for this component type, just once

    def __init__(self, clock_name : str, component_name : str, first_input_signal : Signal, 
                 second_input_signal : Signal, output_signal : Signal) -> None:
        super().__init__(component_name)

        self.first_In = first_input_signal
        self.second_In = second_input_signal
        self.output = output_signal
        self.racine = "adder"

        # list of signals
        self.signals_list : List[Signal] = []
        self.signals_list.extend([self.first_In, self.second_In, self.output])

        # clock 
        clk = Clock.__new__(Clock)
        clk.__init__(clock_name)
        self.signals_list.insert(0, clk)

        # port
        self._Component__generate_ports(self.signals_list)
    
    # -------------------------------------------------------------------
    
    def generate_component_file(self):
        
        if self.first_In.bits >= self.second_In.bits:
            self.output.bits = self.first_In.bits + 1
        else:
            self.output.bits = self.second_In.bits + 1

        # library
        lib = Library.__new__(Library)

        # entity
        entity = f"  \nentity {self.racine} is\n"
        entity += self.port
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
    
    def generate_component_body(self):
        if Adder.first_component == True:
            Adder.first_component = False
            code = ""
            code += f"   component {self.racine} is\n"
            code += f"{self.port}\n"
            code += "   end component;\n"

            for i in self.signals_list:
                code += f"  signal {i.name} : {i.type};\n"
            return code
        
    # -------------------------------------------------------------------
        
    def component_to_vhdl(self):
        # create VHDL file for this components
        if Adder.launch == True:
            self.generate_component_file()
            Adder.launch = False
        return self._Component__generate_component_map()