# Built-in Modules
import json

# Local Modules
from coffee_machine.electrum import Currencies

# Utilities
from coffee_machine.utils import get_file_path


class CurrencyLoader:

    def __init__(self, code: str | int) -> None:
        currencies = Currencies()
        self.currency_id = currencies.get_currency_id(code)
        self.currency_data = self.retrieve_currency_data()

    def retrieve_currency_data(self) -> dict:
        filename = f"{self.currency_id}.{Currencies.extension}"
        filepath = get_file_path(filename, path=Currencies.path)
        with open(filepath, "r", encoding="UTF-8") as currency_file:
            return json.load(currency_file)

    @property
    def data(self):
        return self.currency_data

    @classmethod
    def load(cls, code: str | int) -> dict:
        currency = cls(code)
        return currency.data

# Testing
if __name__ == "__main__":
    pass
