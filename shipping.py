def calculate_Shipping(order_Amount,is_VIP):
    if order_Amount < 0:
        raise ValueError("Order cannot be negative")
    if is_VIP:
        return 0
    if order_Amount < 50:
        return 10
    elif order_Amount < 100:
        return 5
    else:
        return 0
    