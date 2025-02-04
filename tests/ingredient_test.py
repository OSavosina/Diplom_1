from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE
from data.ingredient_data import IngredientData

name = IngredientData.name_mock
price = IngredientData.price_mock
ingredient = INGREDIENT_TYPE_SAUCE

def test_ingredient_get_price_success():
    ingredient_item = Ingredient(ingredient, name, price)
    get_price_result = ingredient_item.get_price()

    assert get_price_result == price and type(price) == float

def test_ingredient_get_name_success():
    ingredient_item = Ingredient(ingredient, name, price)
    get_name_result = ingredient_item.get_name()

    assert get_name_result == name and type(name) == str

def test_ingredient_get_type_success():
    ingredient_item = Ingredient(ingredient, name, price)
    get_type_result = ingredient_item.get_type()

    assert get_type_result == ingredient and type(ingredient) == str