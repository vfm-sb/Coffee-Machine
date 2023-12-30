

def split_by_comma(input_string: str) -> list:
    return [part.strip() for part in input_string.split(",")]


def split_by_colon(input_string: str) -> list:
    return [part.strip() for part in input_string.split(":")]


def split_by_semicolon(input_string: str) -> list:
    return [part.strip() for part in input_string.split(";")]
