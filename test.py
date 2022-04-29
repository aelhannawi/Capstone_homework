import pytest
import main


@pytest.fixture
def happy_cart():
    return [main.CartItem("banana ", 1.99, "Wic Eligible food"),
            main.CartItem("Jordans ", 185.68, "Clothing"),
            main.CartItem("lego star wars set ", 7.29, "Toy")]


def test_happy_mass(happy_cart):
    assert main.get_state_charge("MA ", happy_cart) == 196.21


def test_happy_maine(happy_cart):
    assert main.get_state_charge("ME ", happy_cart) == 205.57


def test_happy_nh(happy_cart):
    assert main.get_state_charge("NH ", happy_cart) == 194.96


def test_negative_cost():
    cart = [main.CartItem("Bananas ", 1.99, "Wic Eligible food"),
            main.CartItem("Jordans ", -185.68, "Clothing"),
            main.CartItem("lego star wars set", 7.29, "Toy")]
    assert main.get_state_charge("MA ", cart) == 196.21


def test_zero_cost():
    cart = [main.CartItem("bananas", 0, "Wic Eligible food")]
    assert main.get_state_charge("MA", cart) == 0


def test_bad_state():
    cart = [main.CartItem("Bananas", 1.99, "Wic Eligible food")]
    assert pytest.raises(ValueError, main.get_state_charge, "Zimbabwe ", cart)


def test_empty_cart():
    cart = []
    assert main.get_state_charge("MA", cart) == 0