# Utilities Imports
from utils import assert_input

# Exceptions
from exceptions import InvalidInputTypeError
from exceptions import InvalidNumericInputError


class InputHandler:

    def __init__(self, input_type: str, prompt: str = "> ", *args, **kwargs) -> None:
        self.input_type = input_type
        self.prompt = prompt
        self.input_method = self.get_input_method()
        self._data = self.input_method(*args, **kwargs)

    @property
    def output(self):
        return self._data

    def get_input_method(self) -> None:
        input_types = {
            "strict-string": self.strict_string_input,
            "loose-string": self.unrestricted_string_input,
            "lower-string": self.lower_string_input,
            "upper-string": self.upper_string_input,
            "menu-code": self.menu_code_input,
        }
        if self.input_type not in input_types:
            raise InvalidInputTypeError
        return input_types[self.input_type]

    def _string_input(self, *args) -> str:
        user_input = input(self.prompt)

        if "assert" in args:
            assert_input(user_input) # MissingInputError
        if "strip" in args:
            user_input = user_input.strip()

        if "lower" in args:
            user_input = user_input.lower()
        elif "upper" in args:
            user_input = user_input.upper()
        elif "swapcase" in args:
            user_input = user_input.swapcase()
        elif "title" in args:
            user_input = user_input.title()
        elif "capitalize" in args:
            user_input = user_input.capitalize()

        return user_input

    def strict_string_input(self) -> str:
        return self._string_input("assert", "strip")

    def unrestricted_string_input(self) -> str:
        return self._string_input()

    def lower_string_input(self) -> str:
        return self._string_input("assert", "strip", "lower")

    def upper_string_input(self) -> str:
        return self._string_input("assert", "strip", "upper")

    def _numeric_input(self) -> int | float:
        numeric_input = self._string_input("assert", "strip")
        try:
            return int(numeric_input)
        except ValueError:
            try:
                return float(numeric_input)
            except ValueError:
                raise InvalidNumericInputError(numeric_input)

    def menu_code_input(self) -> int | float:
        menu_code = self._numeric_input()
        if menu_code < 1:
            raise ValueError(f"Invalid Menu Code >> {menu_code}")
        return menu_code


# Testing
if __name__ == "__main__":
    pass
