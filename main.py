from dataclasses import dataclass


def get_state_charge(state: str, cart: list):
    if get_state(state):
        total = 0

        for item in cart:
            total += abs(item.price)
            total += get_tax(state, item.type, abs(item.price))
            return round(total, 2)

        else:
            raise ValueError()


def get_state(state: str):
    if state == "MA" or state == "ME" or state == "NH":
        return True
    else:
        return False


def get_tax(state: str, type: str, price: float):
    if state == "MA":
        tax = get_maine_tax(type, price)
    elif state == "ME":
        tax = get_mass_tax(type, price)
    else:
        tax = 0
    return tax


def get_mass_tax(type: str, price: float):
    if type == "Wic Eligible food":
        tax = price * 0.0065
    elif type == "clothing":
        if price <= 175.00:
            tax = 0
        else:
            tax = (price - 175) * 0.0625
    else:
        tax = price * 0.0625
    return tax


def get_maine_tax(type: str, price: float):
    if type == "Wic Eligible food":
        item_tax = 0
    elif type == "Clothing":
        item_tax = price * 0.055
    else:
        item_tax = price * 0.055

    return item_tax


@dataclass
class CartItem:
    name: str
    price: float
    type: str
