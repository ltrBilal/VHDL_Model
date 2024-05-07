from a_signal import *
from library import *
from component import *

class Adder(Component):
    In_1 = Signal.__new__(Signal)
    In_2 = Signal.__new__(Signal)
    Out = Signal.__new__(Signal)
    components : list[Component]

    launch = True

    def __init__(self, name, in_signal_1, in_signal_2, out_signal) -> None:
        super().__init__(name)
        self.In_1 = in_signal_1
        self.In_2 = in_signal_2
        self.Out = out_signal

        # clock
        clk = Clk.__new__(Clk)
        clk.__init__("clk")
        # port
        self.port = f"          {clk.signal_to_vhdl()};\n"
        self.port += f"          {self.In_1.signal_to_vhdl()};\n"
        self.port += f"          {self.In_2.signal_to_vhdl()};\n"
        self.port += f"          {self.Out.signal_to_vhdl()}\n"
        # pour generer le code VHDL une seule fois
        adder = Adder.__new__(Adder)
        if adder.launch == True:
            Adder.launch = False
            Adder.generate_vhdl_code(self)
            print("Adder VHDL code generated !!")

    # -------------------------------------------------------------------
    def generate_component_code(port, name):
        code = ""
        code += f"   component {name} is\n"
        code += f"      {port}\n"
        code += "   end component;\n"
        return code
    
    # -------------------------------------------------------------------
    def add_component(self, name):
        comp = self.generate_component_code(self.port, name)
        self.components.append(comp)

    # -------------------------------------------------------------------
    
    def generate_vhdl_code(self):
        
        if self.In_1.bits >= self.In_2.bits:
            self.Out.bits = self.In_1.bits + 1
        else:
            self.Out.bits = self.In_2.bits + 1

        # library
        lib = Library.__new__(Library)

        # entity
        entity = "  \nentity adder is\n"
        entity += "     port \n     (\n"
        entity += self.port
        entity += "     );\nend adder;\n"

        # architecture
        arch = "\narchitecture adder_arch of adder is\n"
        arch += "begin\n"
        arch += f"      {self.Out.name} <= ('0' & {self.In_1.name}) + ('0' & {self.In_2.name});\n"
        arch += "end adder_arch;"

        code += lib.library_vhdl()
        code += entity
        code += arch

        file1 = open('./adder.vhd', 'w')
        file1.write(code)

        # component entity
        comp_entity = f"\nentity adder_tb is \n\n end adder_tb;\n"

        # component architecture
        comp_arch = "\narchitecture adder_tb_arch of adder is\n"
        for i in self.components:
            comp_arch += (f"{i}\n")
        
        