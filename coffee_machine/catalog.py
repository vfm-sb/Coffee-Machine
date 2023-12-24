# Built-in Modules
import json

# Local Modules
from drink import Drink
from catalog_builder import CatalogBuilderCLI

# Utilities Imports
from utils import get_file_path
from utils import valid_filename

# Exceptions
from exceptions import InvalidFilenameError


class Catalog:
    path = "data/catalogs"
    extension = "json"

    def __init__(self, filename: str | None = None) -> None:
        self.filename = filename
        self.filepath = self.get_catalog_filepath()
        self.name = self.get_catalog_name()
        self.catalog_data = self.load_catalog_data()
        self.drinks_data = self.load_drinks_data()
        self.groups_data = self.load_groups_data()

    @property
    def filename(self) -> str:
        return self._filename

    @filename.setter
    def filename(self, filename: str | None = None) -> None:
        if filename is None:
            filename = CatalogBuilderCLI.ask_filename()
        if not valid_filename(string=filename, extension=Catalog.extension):
            raise InvalidFilenameError(filename=filename, extension=Catalog.extension)
        self._filename = filename.lower()

    def get_catalog_name(self) -> str:
        return self.filename.replace("." + Catalog.extension, "").replace("_", " ").lower()

    def get_catalog_filepath(self) -> str:
        return get_file_path(filename=self.filename, path=Catalog.path)

    # Data Loaders
    def load_catalog_data(self) -> dict:
        try:
            with open(self.filepath, "r", encoding="UTF-8") as catalog_file:
                return json.load(catalog_file)
        except FileNotFoundError:
            return {"drinks": {}, "groups": {}}

    def load_drinks_data(self) -> dict:
        drinks_data = {}
        for menu_code, drink_data in self.catalog_data["drinks"].items():
            menu_code = float(menu_code)
            if not self.is_group(menu_code):
                menu_code = int(menu_code)
            drinks_data[menu_code] = Drink.construct(drink_data)
        return drinks_data

    def load_groups_data(self) -> dict:
        groups_data = {}
        for group_code, group_data in self.catalog_data["groups"].items():
            group_code = int(group_code)
            groups_data[group_code] = group_data
        return groups_data

