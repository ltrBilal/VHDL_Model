from a_signal import Signal, Clock
from port import Port
from adder import Adder
from register import Registre
from multiplier import Mult
from model import Model
from component import Connector
from process import Process, Clock_Process
from exception import My_Exception


# model inputs
s1 = Signal("a", 16 , "in")
s2 = Signal("b", 16, "in")
s3 = Signal("c", 17, "in")

# model output
res = Signal("res", 30, "out")

res_int = Signal("res_int", 17, "in")
res_int2 = Signal("res_int2", 17, "in")

clock = Clock("clock", 10, "ns")
clock_tb = Clock("clock_tb", 10, "ns")
clock_tb2 = Clock("clock_tb2", 5, "ns")

port = Port([clock, s1, s2, s3, res])

first_adder = Adder(clock,"first_adder", s1, s2, res)
second_adder = Adder(clock, "second_adder", s1, s2, res)

reg1 = Registre(clock, "reg1", s1, res)

mult = Mult("multip", clock, s1, s2, res)

# Model declaration
m = Model("test")

# add connectors
connector = Connector(first_adder, [clock, s1, s2, res_int])
m.add_connector(connector)

connector2 = Connector(second_adder, [clock,s3 , res_int, res])
m.add_connector(connector2)

reg_connector = Connector(reg1, [clock, s1, res])
m.add_connector(reg_connector)

mult_connector = Connector(mult, [clock, s1, s2, res_int2])
m.add_connector(mult_connector)

# add ports
m.add_port(port)

# add all component
m.add_component(first_adder)
m.add_component(second_adder)
m.add_component(reg1)
m.add_component(mult)

#---------------------------------------------------------------------------
# ERROR : clock can't be used in simulation
""" clk_process = Clock_Process("clock_process", clock)
m.add_process(clk_process) """

# PASS
clk_process2 = Clock_Process("clock_process", clock_tb)
m.add_process(clk_process2)

# ERROR : label already exist
""" clk_process3 = Clock_Process("clock_process", clock_tb2)
m.add_process(clk_process3) """

p = Process("p1", [clock, s1, s2], "wait;")
m.add_process(p)

# create vhdl file (Model.vhd)
m.model_to_vhdl()
