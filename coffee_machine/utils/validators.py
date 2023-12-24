# Built-in Modules
import string


def valid_filename(filename: str, extension: str) -> bool:
    if not filename.endswith("." + extension):
        return False
    for char in filename.replace("." + extension, ""):
        if char not in string.ascii_lowercase + string.digits + "_":
            return False
    return True
