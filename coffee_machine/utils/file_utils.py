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
