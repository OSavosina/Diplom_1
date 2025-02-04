from bun import Bun
from data.bun_data import BunData

name = BunData.name_mock
price = BunData.price_mock

def test_bun_get_name_success():
    bun_item = Bun(name, price)
    get_name_result = bun_item.get_name()

    assert get_name_result == name and type(name) == str


def test_bun_get_price_success():
    bun_item = Bun(name, price)
    get_price_result = bun_item.get_price()

    assert get_price_result == price and type(price) == float