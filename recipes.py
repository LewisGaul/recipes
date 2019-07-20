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
        # TODO: Store the name and list of ingredients on the new object.

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
        # TODO: Write the recipe to file in JSON format. See json.dump().


def read_recipes():
    """
    Read in all recipes we have stored on file.
    """
    # TODO: Read the file of recipe data and return a list of recipes. See json.load().
