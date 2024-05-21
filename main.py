from adder import *
from register import Registre
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
clock_tb2 = Clock("clock_tb2", 5, "ns")

port = Port([clock, s1, s2, s3, res])

first_adder = Adder(clock,"first_adder", s1, s2, res)
second_adder = Adder(clock, "second_adder", s1, s2, res)

reg1 = Registre(clock, "reg1", s1, res)

# Model declaration
m = Model("test")

# add connectors
connector = Connector(first_adder, [clock, s1, s2, res_int])
m.add_connector(connector)

connector2 = Connector(second_adder, [clock,s3 , res_int, res])
m.add_connector(connector2)

reg_connector = Connector(reg1, [clock, s1, res])
m.add_connector(reg_connector)

# add ports
m.add_port(port)

# add all component
m.add_component(first_adder)
m.add_component(second_adder)
m.add_component(reg1)

#---------------------------------------------------------------------------
# ERROR : clock can't be used in simulation
clk_process = Clock_Process("clock_process", clock)
m.add_process(clk_process)

# PASS
clk_process2 = Clock_Process("clock_process", clock_tb)
m.add_process(clk_process2)

# ERROR : label already exist
clk_process3 = Clock_Process("clock_process", clock_tb2)
m.add_process(clk_process3)

p = Process("p1", [clock, s1, s2], "wait;")
m.add_process(p)

# create vhdl file (Model.vhd)
m.model_to_vhdl()

