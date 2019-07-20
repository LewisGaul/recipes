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

        Arguments:
        name
            The name of the recipe.
        ingreds
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
            json.dump([r.to_json() for r in all_recipes], f)


def read_recipes():
    """
    Read in all recipes we have stored on file.
    """
    with open("data.json", "r") as f:
        return [Recipe.from_json(r) for r in json.load(f)]
