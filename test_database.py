import pytest
import database
def test_can_afford_expensive_item(monkeypatch):
     def fake_Balence():
         return 5000
     monkeypatch.setattr(database,"fetch_Real_Balance",fake_Balence)
     result = database.can_Afford_Item(3000)
     assert result == True