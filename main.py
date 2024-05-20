from adder import *
from model import *

# model inputs
s1 = Signal("a", "unsigned(7 downto 0)", "in")
s2 = Signal("b", "unsigned(7 downto 0)", "in")
s3 = Signal("c", "unsigned(7 downto 0)", "in")

# model output
res = Signal("res", "unsigned(8 downto 0)", "out")

res_int = Signal("res_int", "unsigned(7 downto 0)", "in")

clock = Clock("clock", 10, "ns")
clock_tb = Clock("clock_tb", 10, "ns")

port = Port([clock, s1, s2, s3, res])

first_adder = Adder(clock,"first_adder", s1, s2, res)
second_adder = Adder(clock, "second_adder", s1, s2, res)

# Model declaration
m = Model("test")

# add connectors
connector = Connector(first_adder, [clock, s1, s2, res_int])
m.add_connector(connector)

connector2 = Connector(second_adder, [clock,s3 , res_int, res])
m.add_connector(connector2)

# add ports
m.add_port(port)

# add all component
m.add_component(first_adder)
m.add_component(second_adder)

#---------------------------------------------------------------------------
clk_process = Clock_Simulation("clock_process", clock)
m.add_process(clk_process)

clk_process2 = Clock_Simulation("clock_process", clock_tb)
m.add_process(clk_process2)

p = Process("p1", [clock, s1, s2], "wait;")
m.add_process(p)

# create vhdl file (Model.vhd)
m.model_to_vhdl()

""" print("**************************")
for i in m.signals_list:
    print(i.name) """