from adder import *

s1 = Signal.__new__(Signal)
s1.__init__("a", "unsigned(7 downto 0)", "in")

s2 = Signal.__new__(Signal)
s2.__init__("b", "unsigned(7 downto 0)", "in")

s3 = Signal.__new__(Signal)
s3.__init__("res", "unsigned(8 downto 0)", "out")

add = Adder.__new__(Adder)
add.__init__(s1, s2, s3)

add.generate_vhdl_code()