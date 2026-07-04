import pytest
from shipping import calculate_Shipping

@pytest.mark.parametrize("order_Amount,is_VIP,expected_Shipping",[
    (30,False,10),(75,False,5),(150,False,0),(10,True,0),(500,True,0)
])

def test_shipping_costs(order_Amount, is_VIP, expected_Shipping):
    actual_Shipping =calculate_Shipping(order_Amount,is_VIP)
    assert actual_Shipping == expected_Shipping
def test_negative_order():
    with pytest.raises(ValueError):
        calculate_Shipping(-20,False)