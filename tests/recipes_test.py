"""
Tests for recipes.py - run with 'python -m pytest'.
"""

from recipes import Recipe


ingreds = ["tuna", "sweetcorn", "pasta"]


def test_create_recipe():
    """Test creating a recipe works as expected."""
    recipe = Recipe("Tuna pasta", ingreds)
    assert recipe.name == "recipe 1"
    assert recipe.ingreds == ingreds


def test_print_recipe():
    """Test the string representation of a recipe."""
    recipe = Recipe("Tuna pasta", ingreds)
    assert str(recipe) == 'Recipe "Tuna pasta"\n - tuna\n - sweetcorn\n - pasta'
