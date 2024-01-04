# Built-in Modules
import json

# Local Modules
from coffee_machine.electrum import Currency

# Utilities
from coffee_machine.utils import get_file_path

# Exceptions
from coffee_machine.exceptions import CurrencyNotFoundError


class CurrencyLoader:
    path = "data/currencies"
    extension = "json"
    active_currencies = "_CURRENCIES.json"

    def __init__(self, code: str | int) -> None:
        self.currencies = self.load_currencies()
        Currency.assert_currency_code(code)
        if not self.currency_exists(code):
            raise CurrencyNotFoundError
        self.currency_id = self.get_currency_id(code)
        self.currency_data = self.load_currency_data()

    @property
    def data(self):
        return self.currency_data

    def load_currencies(self) -> dict:
        filepath = get_file_path(CurrencyLoader.active_currencies, CurrencyLoader.path)
        with open(filepath, "r", encoding="UTF-8") as active_currencies_file:
            return json.load(active_currencies_file)

    def load_currency_data(self) -> dict:
        filename = f"{self.currency_id}.{CurrencyLoader.extension}"
        filepath = get_file_path(filename, path=CurrencyLoader.path)
        with open(filepath, "r", encoding="UTF-8") as currency_file:
            return json.load(currency_file)

    def get_currency_id(self, code: str | int) -> str | None:
        code = str(code).upper()
        for currency_id, data in self.currencies.items():
            iso_identifiers = (data["iso-alphabetic"], data["iso-numeric"])
            if code in iso_identifiers:
                return currency_id
        return None

    # State Checkers
    def currency_exists(self, code: str | int) -> bool:
        currency_id = self.get_currency_id(code)
        return currency_id in self.currencies


# Testing
if __name__ == "__main__":
    pass
