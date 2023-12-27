"""
Custom Exceptions for Coffee-Machine
"""

# File Operations Exceptions
class InvalidFilenameError(Exception):
    def __init__(self, filename: str | None = None) -> None:
        self.message = "Invalid Filename"
        if filename:
            self.message += f" >> {filename}"
        super().__init__(self.message)


class InvalidInputTypeError(Exception):
    def __init__(self, input_type: str | None) -> None:
        self.message = "Invalid Input Type"
        if input_type:
            self.message += f' >> "{input_type}"'
        super().__init__(self.message)
