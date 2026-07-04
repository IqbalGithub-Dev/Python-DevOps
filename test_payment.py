import pytest
import payment


def test_checkout_Succesful(monkeypatch):
    def fake_Charge(amount):
        return amount

    monkeypatch.setattr(payment, "charge_Credit_Card", fake_Charge)
    final_chekout = payment.checkout_(150)
    assert final_chekout == "Payment accepted ! order  shipped"


def test_checkout_Negative_check(monkeypatch):
    def fake_decline(amount):
        return False

    monkeypatch.setattr(payment, "charge_Credit_Card", fake_decline)
    decline_checkout = payment.checkout_(150)
    assert decline_checkout == "Payment decline"
