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

    def to_json(self):
        """
        Convert the object to JSON format.
        """
        # TODO: Return a dict representation.

    @classmethod
    def from_json(cls, obj):
        """
        Create an instance of the class from a JSON representation.

        :param obj:
            The JSON object.
        :return:
            The created class instance.
        """
        # TODO: Create an instance from JSON.


def read_recipes():
    """
    Read in all recipes we have stored on file.

    :return:
        A list of the recipes found in the data file.
    """
    # TODO: Read the file of recipe data and return a list of recipes. See json.load().
