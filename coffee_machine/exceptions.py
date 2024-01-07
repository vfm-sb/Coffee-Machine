"""
Custom Exceptions for Coffee-Machine
"""

# Generic Object Exceptions
class ObjectMismatchError(TypeError):
    def __init__(self, message: str = "Objects Don't Match") -> None:
        self.message = message
        super().__init__(self.message)


# File Operations Exceptions
class InvalidFilenameError(ValueError):
    def __init__(self, filename: str | None = None) -> None:
        self.message = "Invalid Filename"
        if filename:
            self.message += f" >> {filename}"
        super().__init__(self.message)


# Input Operations Exceptions
class MissingInputError(ValueError):
    def __init__(self) -> None:
        self.message = "Missing Input"
        super().__init__(self.message)


class InvalidInputTypeError(ValueError):
    def __init__(self, input_type: str | None) -> None:
        self.message = "Invalid Input Type"
        if input_type:
            self.message += f' >> "{input_type}"'
        super().__init__(self.message)


class InvalidNumericInputError(ValueError):
    def __init__(self, message: str = "Invalid Numeric Input", input_string: str | None = None) -> None:
        self.message = message
        if input_string:
            self.message += f' >> "{input_string}"'
        super().__init__(self.message)


# Electrum Exceptions
class InvalidCurrencyCodeError(ValueError):
    def __init__(self, message: str = "Invalid Currency Code", code: str | int | None = None) -> None:
        self.message = message
        if code:
            self.message += f" >> {code}"
        super().__init__(self.message)


class CurrencyNotFoundError(FileNotFoundError):
    def __init__(self, message: str = "", code: str | int | None = None) -> None:
        self.message = message
        if code:
            self.message += f" >> {code}"
        super().__init__(self.message)
