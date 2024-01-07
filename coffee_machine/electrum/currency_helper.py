# Utilities
from coffee_machine.utils import get_json_file

# Custom Exceptions
from coffee_machine.exceptions import InvalidCurrencyCodeError
from coffee_machine.exceptions import CurrencyNotFoundError


class CurrencyHelper:
    path = "data/currencies"
    extension = "json"
    all_currencies = "_CURRENCIES.json"

    def __init__(self) -> None:
        self.currencies = self.load_currencies()

    def load_currencies(self) -> dict:
        return get_json_file(CurrencyHelper.all_currencies, CurrencyHelper.path)

    def retrieve_currency_data(self, code: str) -> dict:
        currency_id = self.get_currency_id(code)
        currency_filename = f"{currency_id}.{CurrencyHelper.extension}"
        return get_json_file(currency_filename, path=CurrencyHelper.path)

    def load_currency_data(self, currency_id: str) -> dict:
        if not self.currency_exists(currency_id):
            return CurrencyHelper.empty_dataset()
        return self.retrieve_currency_data(currency_id)

    def get_currency_id(self, code: str | int) -> str | None:
        code = str(code).upper()
        for currency_id, data in self.currencies.items():
            iso_codes = (data["iso-alphabetic"], data["iso-numeric"])
            if code in iso_codes:
                return currency_id
        return None

    def currency_exists(self, code: str | int) -> bool:
        currency_id = self.get_currency_id(code)
        return currency_id in self.currencies

    @staticmethod
    def valid_currency_code(code: str | int) -> bool:
        return CurrencyHelper.valid_alphabetic_code(code) or CurrencyHelper.valid_numeric_code(code)

    @staticmethod
    def valid_alphabetic_code(code: str) -> bool:
        return isinstance(code, str) and code.isalpha() and len(code) == 3

    @staticmethod
    def valid_numeric_code(code: int | str) -> bool:
        return str(code).isdigit() and len(str(code)) == 3

    @staticmethod
    def assert_currency_code(code: str | int) -> None:
        if not CurrencyHelper.valid_currency_code(code):
            raise InvalidCurrencyCodeError(code=code)

    @staticmethod
    def assert_alphabetic_code(code: str) -> None:
        if not CurrencyHelper.valid_alphabetic_code(code):
            raise InvalidCurrencyCodeError("Invalid Alphabetic Currency Code", code=code)

    @staticmethod
    def assert_numeric_code(code: int | str) -> None:
        if not CurrencyHelper.valid_numeric_code(code):
            raise InvalidCurrencyCodeError("Invalid Numeric Currency Code", code=code)

    @staticmethod
    def assert_currency_existance(code: str | int) -> None:
        helper = CurrencyHelper()
        if not helper.currency_exists(code):
            raise CurrencyNotFoundError

    @staticmethod
    def assert_currency(code: str | int) -> None:
        CurrencyHelper.assert_currency_code(code)
        CurrencyHelper.assert_currency_existance(code)

    @staticmethod
    def empty_dataset() -> dict:
        return {
            "iso-alphabetic": None,
            "iso-numeric": None,
            "name": None,
            "base": None,
            "denominator": None,
            "precision": None,
            "unit": {
                "name": None,
                "plural": None,
                "symbol": None,
                "abbreviation": None,
            },
            "subunit": {
                "name": None,
                "plural": None,
                "symbol": None,
                "abbreviation": None,
            },
            "banknotes": [],
            "coins": [],
            "users": [],
        }


# Testing
if __name__ == "__main__":
    pass
