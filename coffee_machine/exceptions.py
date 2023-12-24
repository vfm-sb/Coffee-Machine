# File Operation Exceptions
class InvalidFilenameError(Exception):
    def __init__(self, filename: str | None = None, extension: str | None = None) -> None:
        self.message = f"Invalid Filename: {filename}.{extension}"
        super().__init__(self.message)
