from typing import List
from burger import Burger
from ingredient import Ingredient
from bun import Bun
from data.bun_data import BunData
from ingredient_types import INGREDIENT_TYPE_SAUCE
from data.ingredient_data import IngredientData


def test_set_buns_success():
    burger = Burger()
    bun = Bun(BunData.name_mock, BunData.price_mock)
    burger.set_buns(bun)

    assert burger.bun == bun


def test_add_ingredient_success():
    burger = Burger()
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, IngredientData.name_mock, IngredientData.price_mock)
    burger.ingredients.append(ingredient)

    assert burger.ingredients[0] == ingredient


def test_remove_ingredient_success():
    burger = Burger()
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, IngredientData.name_mock, IngredientData.price_mock)
    burger.ingredients.append(ingredient)
    del burger.ingredients[0]

    assert len(burger.ingredients) == 0


def test_move_ingredient_success():
    burger = Burger()
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, IngredientData.name_mock, IngredientData.price_mock)
    burger.ingredients.append(ingredient)
    burger.ingredients.insert(0, burger.ingredients.pop(0))

    assert burger.ingredients[0] == ingredient


def test_get_price_success():
    burger = Burger()
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, IngredientData.name_mock, IngredientData.price_mock)
    burger.ingredients.append(ingredient)
    bun = Bun(BunData.name_mock, BunData.price_mock)
    burger.set_buns(bun)

    assert burger.get_price() == 300


def test_get_receipt_success():
    burger = Burger()
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, IngredientData.name_mock, IngredientData.price_mock)
    burger.ingredients.append(ingredient)
    bun = Bun(BunData.name_mock, BunData.price_mock)
    burger.set_buns(bun)

    actual_receipt: List[str] = [f'(==== {burger.bun.get_name()} ====)']
    actual_receipt.append(f'= {str(burger.ingredients[0].get_type()).lower()} {burger.ingredients[0].get_name()} =')
    actual_receipt.append(f'(==== {burger.bun.get_name()} ====)\n')
    actual_receipt.append(f'Price: {burger.get_price()}')

    assert burger.get_receipt() == '\n'.join(actual_receipt)



