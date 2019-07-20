"""
Create recipes and save/read them to/from file.
"""

import json


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
        return f'Recipe "{self.name}"\n' + "\n - ".join(self.ingreds)

    def save(self):
        """
        Save the recipe to file.
        """
        # TODO: Write the recipe to file in JSON format. See json.dump().


def read_recipes():
    """
    Read in all recipes we have stored on file.
    """
    # TODO: Read the file of recipe data and return a list of recipes. See json.load().
