# Local Modules
from coffee_machine.electrum import CurrencyLoader

# Exceptions
from coffee_machine.exceptions import ObjectMismatchError
from coffee_machine.exceptions import InvalidCurrencyCodeError


class Currency:

    def __init__(self, code: str | int) -> None:
        currency_data = CurrencyLoader(code).data
        self.alphabetic_code = currency_data["iso-alphabetic"]
        self.numeric_code = currency_data["iso-numeric"]
        self.name = currency_data["name"]
        self.base = currency_data["base"]
        self.denominator = currency_data["denominator"]
        self.precision = currency_data["precision"]
        self.unit_name = currency_data["unit"]["name"]
        self.unit_plural = currency_data["unit"]["plural"]
        self.unit_symbol = currency_data["unit"]["symbol"]
        self.unit_abbr = currency_data["unit"]["abbreviation"]
        self.unit_symbol_format = currency_data["unit"]["formats"]["symbol"]
        self.unit_abbr_format = currency_data["unit"]["formats"]["abbreviation"]
        self.subunit_name = currency_data["subunit"]["name"]
        self.subunit_plural = currency_data["subunit"]["plural"]
        self.subunit_symbol = currency_data["subunit"]["symbol"]
        self.subunit_abbr = currency_data["subunit"]["abbreviation"]
        self.subunit_symbol_format = currency_data["subunit"]["formats"]["symbol"]
        self.subunit_abbr_format = currency_data["subunit"]["formats"]["abbreviation"]
        self.banknotes = currency_data["banknotes"]
        self.coins = currency_data["coins"]
        self.users = currency_data["users"]

    def __hash__(self) -> int:
        return hash((self.alphabetic_code, self.numeric_code))

    def __eq__(self, other: 'Currency') -> bool:
        if not isinstance(other, Currency):
            raise ObjectMismatchError(f"Currency Object Mismatch >> {type(other)}")
        return self.alphabetic_code == other.alphabetic_code

    def __ne__(self, other: 'Currency') -> bool:
        return not self == other

    # Helper Methods
    @staticmethod
    def valid_currency_code(code: str | int) -> bool:
        return Currency.valid_alphabetic_code(code) or Currency.valid_numeric_code(code)

    @staticmethod
    def valid_alphabetic_code(code: str) -> bool:
        return isinstance(code, str) and code.isalpha() and len(code) == 3

    @staticmethod
    def valid_numeric_code(code: int | str) -> bool:
        return str(code).isdigit() and len(str(code)) == 3

    @staticmethod
    def assert_currency_code(code: str | int) -> None:
        if not Currency.valid_currency_code(code):
            raise InvalidCurrencyCodeError


# Testing
if __name__ == "__main__":
    pass
