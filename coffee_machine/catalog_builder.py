# Local Modules
from catalog import Catalog
from drink import Drink
from input_handler import InputHandler

# Utilities Imports
from utils import convert_to_filename
from utils import custom_title
from utils import valid_filename

# Exceptions
from exceptions import MissingInputError
from exceptions import InvalidNumericInputError


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
            input_string = InputHandler(input_type="lower-string").output
        except MissingInputError as error_message:
            print(error_message)
            print()
            return CatalogBuilderCLI.ask_filename()

        if valid_filename(input_string, extension="json"):
            return input_string
        return convert_to_filename(name=input_string, extension=CatalogBuilderCLI.extension)

    def ask_menu_code(self, currenct_code: int | float | None = None) -> int | float:
        print(f'{"Enter" if not currenct_code else "Change"} Menu Code')
        if currenct_code:
            print(f"Current Menu Code is {currenct_code}")
        try:
            menu_code = InputHandler(input_type="menu-code").output
        except (InvalidNumericInputError, ValueError) as error_message:
            print(error_message)
            print()
            return self.ask_menu_code(currenct_code)
        if self.menu_code_taken(menu_code) and menu_code != currenct_code:
            return self.ask_menu_code(currenct_code)
        return menu_code

    def ask_drink_name(self, current_name: str | None = None) -> str:
        print(f'{"Enter" if not current_name else "Change"} Drink Name')
        if current_name:
            print(f"Current Drink Name is {current_name}")
        try:
            drink_name = InputHandler(input_type="lower-string").output
        except MissingInputError as error_message:
            print(error_message)
            print()
            return self.ask_drink_name(current_name)
        if self.drink_exist(drink_name):
            print(f"{custom_title(drink_name)} Already Exists! Try A Different Drink Name.")
            print()
            return self.ask_drink_name(current_name)
        return drink_name

    def ask_group_name(self, current_name: str | None = None) -> str:
        print(f'{"Enter" if not current_name else "Change"} Drink Name')
        if current_name:
            print(f"Current Drink Name is {current_name}")
        try:
            group_name = InputHandler(input_type="lower-string").output
        except MissingInputError as error_message:
            print(error_message)
            print()
            return self.ask_group_name(current_name)
        return group_name

    def ask_ingredients(self, current_ingredients: dict | None = None) -> dict:
        print(f"{'Enter' if not current_ingredients else 'Change'} Ingredients:")
        if current_ingredients:
            print(f"Current Ingredients are {Drink.display_ingredients(current_ingredients)}")
        exit_keywords = ["done"]
        ingredients = InputHandler(input_type="ingredients", exit_keywords=exit_keywords).output
        if len(ingredients) == 0:
            print("Empty Collection! Data Input Required.")
            return self.ask_ingredients(current_ingredients)
        return ingredients

