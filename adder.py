from a_signal import *
from library import *

class Adder:
    In_1 = Signal.__new__(Signal)
    In_2 = Signal.__new__(Signal)
    Out = Signal.__new__(Signal)


    def __init__(self, in_signal_1, in_signal_2,out_signal) -> None:
        self.In_1 = in_signal_1
        self.In_2 = in_signal_2
        self.Out = out_signal

    def generate_vhdl_code(self):
        code = ""

        if self.In_1.bits >= self.In_2.bits:
            self.Out.bits = self.In_1.bits + 1
        else:
            self.Out.bits = self.In_2.bits + 1

        # library
        lib = Library.__new__(Library)

        # clock
        clk = Clk.__new__(Clk)
        clk.__init__("clk")

        # port
        port = f"          {clk.signal_to_vhdl()};\n"
        port += f"          {self.In_1.signal_to_vhdl()};\n"
        port += f"          {self.In_2.signal_to_vhdl()};\n"
        port += f"          {self.Out.signal_to_vhdl()}\n"


        # entity
        entity = "  \nentity adder is\n"
        entity += "     port \n     (\n"
        entity += port
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