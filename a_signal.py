class Signal:
    bits = 8

    def __init__(self, name : str, type : str, direction : str) -> None:
        self.name : str = name
        self.type : str = type
        if direction not in ("in", "out", None):
            raise ValueError("Direction must be 'in', 'out' or 'None'")
        self.direction : str = direction

    def signal_to_vhdl(self):
        if self.direction == None:
            return f"signal {self.name} : {self.type}"
        else:
            return f"{self.name} : {self.direction} {self.type}"

    def copy(self):
        return Signal(self.name, self.type, self.direction)

#-------------------------------------------------------------

class Clock(Signal):
    type = "std_logic"
    direction = "in"

    def __init__(self, name : str, period : int, unit : str) -> None:
        self.name = name
        self.period = period
        self.unit = unit