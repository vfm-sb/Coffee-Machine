# Local Modules
from catalog import Catalog


class CatalogBuilderCLI(Catalog):

    def __init__(self, filename: str | None = None) -> None:
        super().__init__(filename)
        if not self.empty_catalog():
            self.modify_catalog()

    def build_catalog(self):
        pass

    def modify_catalog(self):
        pass
