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
