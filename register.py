from a_signal import Signal

class Registre:
    name = None
    bits = 8

    In = Signal.__new__(Signal)
    Out = Signal.__new__(Signal)

    def __init__(self, name) -> None:
        self.name = name
        self.In.__init__(f"{self.name}_in", "unsigned("f"{self.bits - 1} downto 0)", "in")
        self.Out.__init__(f"{self.name}_out", "unsigned("f"{self.bits - 1} downto 0)", "out")

    def __init__(self, name, bits) -> None:
        self.name = name
        self.bits = bits
        self.In.__init__(f"{self.name}_in", "unsigned("f"{self.bits - 1} downto 0)", "in")
        self.Out.__init__(f"{self.name}_out", "unsigned("f"{self.bits - 1} downto 0)", "out")

    