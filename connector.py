from component import *

class Connector:

    def __init__(self, component : Component, signals_list : List[Signal]) -> None:
        self.component = component
        self.signals_list = signals_list