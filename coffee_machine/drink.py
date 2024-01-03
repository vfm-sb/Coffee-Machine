

class Drink:

    def __init__(
        self, name: str, ingredients: dict, sweeteners: list, extras: dict
    ) -> None:
        self.name = name
        self.ingredients = ingredients
        self.sweeteners = sweeteners
        self.extras = extras

    def get_drink_data(self) -> dict:
        return {
            "name": self.name,
            "ingredients": self.ingredients,
            "sweeteners": self.sweeteners,
            "extras": self.extras
        }

    @classmethod
    def construct(cls, drink_data: dict) -> 'Drink':
        return cls(
            name = drink_data["name"],
            ingredients = drink_data["ingredients"],
            sweeteners = drink_data["sweeteners"],
            extras = drink_data["extras"]
        )


# Testing
if __name__ == "__main__":
    pass
