import pytest
from ticket import get_ticket_Price
@pytest.mark.parametrize("age,expected_price",[
    (10,5),(30,15),(75,10)
])

def test_ticket_pricing(age, expected_price):
    actual_Price = get_ticket_Price(age)
    assert actual_Price == expected_price

def test_negative_age():
    with pytest.raises(ValueError):
        get_ticket_Price(-5), "Negative age cant be possible"