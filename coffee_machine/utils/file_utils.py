# Built-in Modules
import os


def get_root_path() -> str:
    current_script_path = os.path.abspath(__file__)
    utils_path = os.path.dirname(current_script_path)
    project_path = os.path.dirname(utils_path)
    project_root = os.path.dirname(project_path)
    return project_root


def get_folder_path(path: str) -> str:
    return get_root_path() + "/" + path + "/"


def get_file_path(filename: str, path: str) -> str:
    return get_folder_path(path) + filename


def file_exists(filename: str, path: str) -> bool:
    file_path = get_file_path(filename, path)
    return os.path.exists(file_path)


def list_files(path: str, extension: str | None = None, excluded: list | None = None) -> list:
    if extension is None:
        extension = ""
    if excluded is None:
        excluded = []
    all_files = os.listdir(get_folder_path(path))
    filtered_files = []
    for file in all_files:
        if file in excluded:
            continue
        if file.endswith(extension):
            filtered_files.append(file)
    return filtered_files


# Testing
if __name__ == "__main__":
    pass
