# Local Modules
from catalog import Catalog
from input_handler import InputHandler

# Utilities Imports
from utils import convert_to_filename
from utils import valid_filename


class CatalogBuilderCLI(Catalog):

    def __init__(self, filename: str | None = None) -> None:
        super().__init__(filename)
        if not self.empty_catalog():
            self.modify_catalog()

    def build_catalog(self):
        pass

    def modify_catalog(self):
        pass

    @staticmethod
    def ask_filename() -> str:
        print("Enter Catalog Name or Filename:")
        try:
            input_string = InputHandler(input_type="string").data
        except ValueError as error_message:
            print(error_message)
            print()
            return CatalogBuilderCLI.ask_filename()

        if valid_filename(input_string, extension="json"):
            return input_string
        return convert_to_filename(name=input_string, extension=CatalogBuilderCLI.extension)
