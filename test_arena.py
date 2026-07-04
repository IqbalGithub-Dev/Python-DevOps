import pytest
from arena import fighter

def test_negative_fightter_life():
    hero = fighter("Cuffi",health=20,attack_power=30)
    hero.take_damage(50)
    assert hero.health >=0, f"BUG FOUND: Health dropped to {hero.health}!"