# Local Modules
from coffee_machine.electrum import CurrencyHelper


class CurrencyLoader(CurrencyHelper):

    def __init__(self, code: str) -> None:
        super().__init__()
        CurrencyHelper.assert_currency(code)
        self.currency_data = self.retrieve_currency_data(code)

    @classmethod
    def load(cls, code: str | int) -> dict:
        currency = cls(code)
        return currency.currency_data


# Testing
if __name__ == "__main__":
    pass
