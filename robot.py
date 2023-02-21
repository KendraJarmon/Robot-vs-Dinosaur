from weapons import Weapon

class Robot:
    def __init__(self):
        self.name1 = 'Ray'
        self.health = 100
        self.attack_weapon = Weapon()

    def attack(self, Dinosaur):
        Dinosaur.health -= self.attack_weapon.attack_power
        print(self)