"""
Create recipes and save/read them to/from file.
"""

import json
import logging


class Recipe:
    """
    Representation of a recipe object.
    """

    def __init__(self, name, ingreds):
        """
        Initialise the recipe instance.

        :param name:
            The name of the recipe.
        :param ingreds:
            A list of ingredients required for the recipe.
        """
        self.name = name
        self.ingreds = ingreds

    def __str__(self):
        """
        Define how to print a recipe object.
        """
        lines = [f'Recipe "{self.name}"'] + [f" - {i}" for i in self.ingreds]
        return "\n".join(lines)

    def save(self):
        """
        Save the recipe to file. If a recipe of the same name already exists a warning is logged and
        this recipe is not saved.
        """
        all_recipes = read_recipes()
        if self.name in [r.name for r in all_recipes]:
            logging.warning(f"Recipe with name '{self.name}' already exists, not saving")
            return
        all_recipes.append(self)
        with open("data.json", "w") as f:
            json.dump([r.to_json() for r in all_recipes], f, indent=4)

    def to_json(self):
        """
        Convert the object to JSON format.
        """
        return {"name": self.name, "ingredients": [str(i) for i in self.ingreds]}

    @classmethod
    def from_json(cls, obj):
        """
        Create an instance of the class from a JSON representation.

        :param obj:
            The JSON object.
        :return:
            The created class instance.
        """
        return cls(obj["name"], obj["ingredients"])


def read_recipes():
    """
    Read in all recipes we have stored on file.

    :return:
        A list of the recipes found in the data file.
    """
    with open("data.json", "r") as f:
        return [Recipe.from_json(r) for r in json.load(f)]
