# Built-in Modules
import json

# Utilities
from coffee_machine.utils import get_file_path


class Currencies:
    path = "data/currencies"
    extension = "json"
    active_currencies = "_CURRENCIES.json"

    def __init__(self) -> None:
        self._currencies = self.load_currencies()

    def load_currencies(self) -> dict:
        filepath = get_file_path(Currencies.active_currencies, Currencies.path)
        with open(filepath, "r", encoding="UTF-8") as active_currencies_file:
            return json.load(active_currencies_file)

    def get_currencies(self) -> dict:
        return self._currencies

    def get_currency_id(self, code: str | int) -> str | None:
        code = str(code).upper()
        for currency_id, data in self._currencies.items():
            iso_identifiers = (data["iso-alphabetic"], data["iso-numeric"])
            if code in iso_identifiers:
                return currency_id
        return None

    def currency_exists(self, code: str | int) -> bool:
        currency_id = self.get_currency_id(code)
        return currency_id in self._currencies


# Testing
if __name__ == "__main__":
    pass
