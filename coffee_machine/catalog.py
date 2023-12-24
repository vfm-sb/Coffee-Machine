# Local Modules
from catalog_builder import CatalogBuilderCLI
# Utilities Imports
from utils import valid_filename
from exceptions import InvalidFilenameError


class Catalog:
    extension = "json"
    def __init__(self, filename: str | None = None) -> None:
        self.filename = filename

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

