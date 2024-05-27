from typing import List
from colors import colors

class My_Exception:
    exceptions_list : List[Exception] = []
    warnings_list : List[Warning] = []

    @classmethod
    def add_exception(cls, e : Exception) -> None:
        cls.exceptions_list.append(e)

    @classmethod
    def add_warning(cls, w : Warning) -> None:
        cls.warnings_list.append(w)
    
    @classmethod
    def display_exceptions(cls) -> None:
        for e in cls.exceptions_list:
            print(f"{colors.RED} {e} {colors.END}")

    @classmethod
    def display_warnings(cls) -> None:
        for w in cls.warnings_list:
            print(f"{colors.YELLOW} {w} {colors.END}")
