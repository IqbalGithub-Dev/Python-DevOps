class Bank_Account:
    def __init__(self,Account_Holder,balance):
        self.Account_Holder = Account_Holder
        self.balance = balance
    
    def withdraw(self,amount):
        if type(amount) not in [int, float]:
            # If it is a string, we manually trigger a TypeError
            raise TypeError("Please enter a valid number, not text.")
        if amount > self.balance:
            print("With draw cant be possible")
            return
        self.balance -= amount
        print(f"Rupees{ amount} was debited from your account")
    
    def deposit(self,amount):
        if type(amount) not in [int, float]:
            # If it is a string, we manually trigger a TypeError
            raise TypeError("Please enter a valid number, not text.")
        if amount <= 0:
            print("Negative amount cannot be deposited")
            return
        self.balance += amount
        print(f"Rupees {amount} was credited in your account")

# Person1 = Bank_Account("Iqbal",1000)
# print(Person1.Account_Holder)
# print(Person1.balance)

# Person1.deposit(1000)
# print(Person1.balance)