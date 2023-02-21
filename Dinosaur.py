class Dinosaur:
    def __init__(self):
        self.name = 'Larry'
        self.health = 100
        self.attack_power = 45
        self.attack_power2 = 60

    def attack(self, robot):
        robot.health -= self.attack_power
        print(self)