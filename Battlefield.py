from Dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.battle_robot = Robot()
        self.battle_Dinosaur = Dinosaur()
    import weapons

    def run_game(self):
       self.display_welcome()
       self.battle_phase()
       self.display_winner()


    def display_welcome(self):
        print('\nWelcome to the first of many epic battle!\there can only be one Champion!\n')

    def battle_phase(self):
        self.battle_Dinosaur.attack(self.battle_robot)
        self.battle_robot.attack(self.battle_Dinosaur)


    def display_winner(self):
      pass