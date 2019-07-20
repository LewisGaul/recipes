"""
Tests for recipes.py - run with 'python -m pytest'.
"""

from recipes import Recipe, read_recipes


ingreds = ["tuna", "sweetcorn", "pasta"]


def test_create_recipe():
    """Test creating a recipe works as expected."""
    recipe = Recipe("Tuna pasta", ingreds)
    assert recipe.name == "Tuna pasta"
    assert recipe.ingreds == ingreds


def test_print_recipe():
    """Test the string representation of a recipe."""
    recipe = Recipe("Tuna pasta", ingreds)
    assert str(recipe) == 'Recipe "Tuna pasta"\n - tuna\n - sweetcorn\n - pasta'


def test_recipe_to_json():
    """Test converting a recipe to JSON format."""
    recipe = Recipe("Tuna pasta", ingreds)
    data = recipe.to_json()
    assert data["name"] == recipe.name
    assert data["ingredients"] == recipe.ingreds


def test_recipe_from_json():
    """Test creating a recipe from JSON format."""
    orig_recipe = Recipe("Tuna pasta", ingreds)
    new_recipe = Recipe.from_json(orig_recipe.to_json())
    assert new_recipe.name == orig_recipe.name
    assert new_recipe.ingreds == orig_recipe.ingreds


def test_read_data():
    """Test reading in recipes works."""
    recipes = read_recipes()
    assert len(recipes) == 2
    assert type(recipes[0]) == Recipe
    assert recipes[0].name == "Tuna pasta"
    assert recipes[0].ingreds == ingreds
    assert recipes[1].name == "Tomato pasta"


def test_save_recipe(mock_json_dump):
    """Test saving a recipe works."""
    expected_recipes = read_recipes()
    recipe = Recipe("new recipe", ["banana", "apple"])
    recipe.save()
    expected_recipes.append(recipe)
    mock_json_dump.assert_called_once()
    assert mock_json_dump.call_args[0][0] == [r.to_json() for r in expected_recipes]
