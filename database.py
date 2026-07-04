import time
def fetch_Real_Balance():
    print("\n connecting to the bank server.....Please wait")
    time.sleep(5)
    return 100

def can_Afford_Item(price):
    balance = fetch_Real_Balance()
    if balance >= price:
        return True
    return False