import pytest
from bank import Bank_Account

def test_cannot_overdraft():
    account = Bank_Account("Iqbal",100)
    account.withdraw(500)
    assert account.balance >= 0 , f"SECURITY FLAW: Account went into negative! Balance is {account.balance}"

def test_cannot_deposit_negative_money():
    account = Bank_Account("sohail",100)
    account.deposit(-50)
    assert account.balance == 100
    
def test_with_string_rise_error():
    account = Bank_Account("cuffii",100)
    with pytest.raises(TypeError):
        account.withdraw("fifty")