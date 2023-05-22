from Dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.battle_robot = Robot()
        self.battle_Dinosaur = Dinosaur()
    

    def run_game(self):
       self.display_welcome()
       self.battle_phase()
       self.display_winner()


    def display_welcome(self):
        print('\nWelcome to the first of many epic battle!\there can only be one Champion!\n')

    def battle_phase(self):
        while self.battle_Dinosaur.health > 0 and self.battle_robot.health > 0:
            self.battle_Dinosaur.attack(self.battle_robot)
            if(self.battle_robot> 0):
                self.battle_robot.attack(self.battle_Dinosaur)


    def display_winner(self):
        if(self.battle_Dinosaur.health > 0):
            print("Dinosaur Wins")
        else:
            print("Robot Wins")