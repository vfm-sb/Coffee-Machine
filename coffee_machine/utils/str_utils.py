# Built-in Modules
import string


def convert_to_filename(name: str, extension: str) -> str:
    base_filename = ""
    for char in name.strip():
        if char in string.ascii_letters + string.digits + string.whitespace:
            base_filename += char.lower()
    base_filename = base_filename.replace(" ", "_")
    return f"{base_filename}.{extension}"


def convert_to_name(filename: str, extension: str) -> str:
    return filename.replace("." + extension, "").replace("_", " ").lower()
