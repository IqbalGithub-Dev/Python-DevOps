class shopping_Cart:
    def __init__(self):
        self.total_price = 0
    def add_to_Cart(self,price):
        if price < 0:
            raise ValueError("SECURITY ERROR NEGATIVE PRICE")
        self.total_price += price
    def discount_Coupon(self,percentage):
        if percentage > 100:
            print("Please Enter valid Coupoun")
            return
        discount_amount = self.total_price * (percentage/100)
        self.total_price -= discount_amount