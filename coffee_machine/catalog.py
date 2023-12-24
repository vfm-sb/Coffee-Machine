# Local Modules
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

