from adder import *
from model import *

s1 = Signal("a", "unsigned(7 downto 0)", "in")

s2 = Signal("b", "unsigned(7 downto 0)", "in")

s3 = Signal("res", "unsigned(8 downto 0)", "out")

add = Adder("clock", "first_adder", s1, s2, s3)

add2 = Adder("clock", "second_adder", s1, s2, s3)

m = Model("test")

# add all component
m.add_component(add)
m.add_component(add2)

# create vhdl file (Model.vhd)
m.model_to_vhdl()