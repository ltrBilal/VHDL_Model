from adder import *
from model import *

s1 = Signal("a", "unsigned(7 downto 0)", "in")
s2 = Signal("b", "unsigned(7 downto 0)", "in")
k_int = Signal("k_int", "unsigned(7 downto 0)", "in")

res = Signal("res", "unsigned(8 downto 0)", "out")

clock = Clock("clk")

port = Port([clock, s1, s2, res])

add = Adder(clock,"first_adder", s1, s2, res)
add2 = Adder(clock, "second_adder", s1, s2, res)

# Model declaration
m = Model("test")

# add connectors
connector = Connector(add, [clock, k_int, s2, res])
m.add_connector(connector)

"""
connector2 = Connector(add2, [clock, k_int, s2, res])
m.add_connector(connector2)
"""

# add ports
m.add_port(port)

# add all component
m.add_component(add)
m.add_component(add2)

# create vhdl file (Model.vhd)
m.model_to_vhdl()

