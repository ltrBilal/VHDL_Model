class Signal:
    bits = 8

    def __init__(self, name, type, direction) -> None:
        self.name = name
        self.type = type
        self.direction = direction

    def signal_to_vhdl(self):
        if self.direction == None:
            return f"signal {self.name} : {self.type}"
        else:
            return f"{self.name} : {self.direction} {self.type}"

#-------------------------------------------------------------

class Clock(Signal):
    period = "10 us"
    type = "std_logic"
    direction = "in"

    def __init__(self, name) -> None:
        self.name = name