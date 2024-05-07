from a_signal import Signal
from abc import ABC, abstractmethod

class Component:
    name : None
    port : None
    
    def __init__(self, name) -> None:
        self.name = name
    
    @abstractmethod
    def add_component(self, name):
        pass

    @abstractmethod
    def generate_vhdl_code(self):
        pass

    @abstractmethod
    def generate_component_code(self, name):
        pass