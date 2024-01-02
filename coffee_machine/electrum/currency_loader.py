# Local Modules
from coffee_machine.electrum import Currency

# Exceptions
from coffee_machine.exceptions import InvalidCurrencyCodeError, CurrencyNotFoundError


class CurrencyLoader:

    def __init__(self, code: str | int) -> None:
        self.currencies = self.load_currencies()
        if not Currency.valid_currency_code(code):
            raise InvalidCurrencyCodeError
        if not self.currency_exists(code):
            raise CurrencyNotFoundError
        self.currency_id = self.get_currency_id(code)
        self.currency_data = self.load_currency_data()

