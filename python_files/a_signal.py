from exception import My_Exception

class Signal:
    """
        Signal class

        Attributes:
            name (str): signal name
            type (str): signal type
            number_of_bits (int): number of bits if the signal or 'None'
            direction (str): it can take 'in', 'out' or None as values
    """

    def __init__(self, name : str, type_or_number_of_bits : str | int, direction : str) -> None:
        """
            Signal constrector

            args:
                name (str): signal name
                type_or_number_of_bits (str | int): it can be the type or the number of bits of a signal
                direction (str): it can take 'in', 'out' or None as values

            returns:
                None  
        """
        self.name : str = name
        self.number_of_bits : int = None
        # verify the type of the signal (int or str)
        try:
            number_of_bits = int(type_or_number_of_bits)
        except ValueError:
            self.type : str = type_or_number_of_bits # if the type is a string
        else:
            try:
                self.number_of_bits = number_of_bits
                # if the type is an integer
                if number_of_bits == 1:
                    self.type = "std_logic"
                elif number_of_bits > 1:
                    self.type = f"unsigned({number_of_bits - 1} downto 0)"
                else:
                    self.type = None
                    raise ValueError("ERROR : number of bits cannot be negative")
            except ValueError as e:
                My_Exception.add_exception(e)

        # if direction not valide
        try:
            if direction not in ("in", "out", None):
                raise ValueError("Direction must be 'in', 'out' or 'None'")
        except ValueError as e:
            My_Exception.add_exception(e)
        self.direction : str = direction

    def signal_to_vhdl(self) -> str:
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