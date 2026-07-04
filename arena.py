class fighter:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
