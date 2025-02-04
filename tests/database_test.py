from database import Database


def test_available_buns_success():
    database = Database()

    assert database.available_buns() == database.buns

def test_available_ingredients_success():
    database = Database()

    assert database.available_ingredients() == database.ingredients