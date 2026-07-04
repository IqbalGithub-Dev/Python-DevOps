import time

def charge_Credit_Card(amount):
    print(f"Danger ! your credit card has been charge for {amount}")
    time.sleep(5)
    return True

def checkout_(cart_total):
    print("starting checkout")
    payment_Succesful = charge_Credit_Card(cart_total)
    if payment_Succesful:
        return "Payment accepted ! order  shipped"
    else:
        return "Payment decline"