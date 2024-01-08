# Local Modules
from coffee_machine.electrum import CurrencyHelper

# Utilities Imports
from coffee_machine.utils import assert_input
from coffee_machine.utils import get_numeric_value, get_integer_value, extract_numeric_value
from coffee_machine.utils import split_by_comma, split_by_colon, split_by_semicolon

# Exceptions
from coffee_machine.exceptions import InvalidInputTypeError


class InputHandler:

    def __init__(self, input_type: str, prompt: str = "> ", **kwargs) -> None:
        self.input_type = input_type
        self.prompt = prompt
        self.input_method = self.get_input_method()
        self._data = self.input_method(**kwargs)

    @property
    def output(self):
        return self._data

    def get_input_method(self) -> None:
        input_types = {
            "strict-string": self.strict_string_input,
            "loose-string": self.loose_string_input,
            "unrestricted-string": self.unrestricted_string_input,
            "lower-string": self.lower_string_input,
            "upper-string": self.upper_string_input,
            "numeric": self.numeric_input,
            "integer": self.integer_input,
            "loose-numeric": self.loose_numeric_input,
            "multiple-numeric": self.multiple_numeric_values_input,
            "menu-code": self.menu_code_input,
            "ingredients": self.ingredients_input,
            "currency-code": self.currency_code_input,
            "alphabetic-currency-code": self.alphabetic_currency_code_input,
            "numeric-currency-code": self.numeric_currency_code_input,
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

    def loose_string_input(self) -> str:
        return self._string_input("lower")

    def unrestricted_string_input(self) -> str:
        return self._string_input()

    def lower_string_input(self) -> str:
        return self._string_input("assert", "strip", "lower")

    def upper_string_input(self) -> str:
        return self._string_input("assert", "strip", "upper")

    def numeric_input(self) -> int | float:
        user_input = self._string_input("assert", "strip")
        return get_numeric_value(input_string=user_input)

    def integer_input(self) -> int:
        user_input = self._string_input("assert", "strip")
        return get_integer_value(user_input)

    def loose_numeric_input(self) -> int | float | str:
        user_input = self._string_input("assert", "strip")
        try:
            return get_numeric_value(input_string=user_input)
        except ValueError:
            return user_input

    def multiple_numeric_values_input(self, exit_keywords: list | None = None, duplicates: bool = True) -> list:
        if not exit_keywords:
            exit_keywords = ["done", "exit", "eol"]
        numeric_values = []
        while True:
            user_input = self.loose_numeric_input()
            if user_input in exit_keywords:
                break
            if "," in user_input:
                input_values = split_by_comma(user_input)
                numeric_values.extend(input_values)
            else:
                numeric_values.append(user_input)
        if not duplicates:
            numeric_values = list(set(numeric_values))
        return numeric_values

    def menu_code_input(self) -> int | float:
        menu_code = self.numeric_input()
        if menu_code < 1:
            raise ValueError(f"Invalid Menu Code >> {menu_code}")
        return menu_code

    def ingredients_input(self, exit_keywords: dict | None = None) -> dict:
        if not exit_keywords:
            exit_keywords = ["done", "exit", "eol"]
        ingredients_data = {}
        while True:
            user_input = self.lower_string_input()
            if user_input in exit_keywords:
                break
            if "," in user_input:
                ingredients = split_by_comma(user_input)
                for ingredient_string in ingredients:
                    raw_ingredient_amount, ingredient_name = ingredient_string.split()
                    ingredient_amount = extract_numeric_value(raw_ingredient_amount)
                    ingredients_data[ingredient_name] = ingredient_amount
            elif ";" in user_input:
                ingredients = split_by_semicolon(user_input)
                for ingredient_string in ingredients:
                    ingredient_name, raw_ingredient_amount = split_by_colon(ingredient_string)
                    ingredient_amount = extract_numeric_value(raw_ingredient_amount)
                    ingredients_data[ingredient_name] = ingredient_amount
            elif ":" in user_input:
                ingredient_name, raw_ingredient_amount = split_by_colon(user_input)
                ingredient_amount = extract_numeric_value(raw_ingredient_amount)
                ingredients_data[ingredient_name] = ingredient_amount
            else:
                ingredient_name = user_input
                raw_ingredient_amount = self.lower_string_input()
                ingredient_amount = extract_numeric_value(raw_ingredient_amount)
                ingredients_data[ingredient_name] = ingredient_amount
        return ingredients_data

    def currency_code_input(self) -> str:
        user_input = self.upper_string_input()
        CurrencyHelper.assert_currency_code(user_input) # InvalidCurrencyCodeError
        return user_input

    def alphabetic_currency_code_input(self) -> str:
        user_input = self.upper_string_input()
        CurrencyHelper.assert_alphabetic_code(user_input) # InvalidCurrencyCodeError
        return user_input

    def numeric_currency_code_input(self) -> str:
        user_input = self.strict_string_input()
        CurrencyHelper.assert_numeric_code(user_input) # InvalidCurrencyCodeError
        return user_input


# Testing
if __name__ == "__main__":
    pass
