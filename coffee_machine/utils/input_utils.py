# Exceptions
from exceptions import InvalidNumericInputError


def get_numeric_value(input_string: str) -> int | float:
    try:
        return int(input_string)
    except ValueError:
        try:
            return float(input_string)
        except ValueError:
            raise InvalidNumericInputError(input_string)


def split_by_comma(input_string: str) -> list:
    return [part.strip() for part in input_string.split(",")]


def split_by_colon(input_string: str) -> list:
    return [part.strip() for part in input_string.split(":")]


def split_by_semicolon(input_string: str) -> list:
    return [part.strip() for part in input_string.split(";")]
