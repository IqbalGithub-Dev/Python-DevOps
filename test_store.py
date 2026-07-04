import pytest
from store import shopping_Cart
def test_hacker_negative_cart():
    my_Cart = shopping_Cart()
    with pytest.raises(ValueError):
        my_Cart.add_to_Cart(-50)
    

def test_discount_limit():
    my_Cart = shopping_Cart()
    my_Cart.add_to_Cart(100)
    my_Cart.discount_Coupon(150)
    assert my_Cart.total_price >=0 , "cart caant be negative"