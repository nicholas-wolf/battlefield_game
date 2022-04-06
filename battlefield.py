
from dinosaur import Dinosaur
from robot import Robot
from weapon import Weapon



class Battlefield:
    def __init__(self):
        self.robot = Robot("Mecha")
        self.dinosaur = Dinosaur("T-Rex", 25)
        
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        

    def display_welcome(self):
        print("Welcome to Battlefield")

    def battle_phase(self):
        while self.dinosaur.health > 0 or self.robot.health > 0:
            self.dinosaur.attack(self.robot)
            if self.robot.health > 0:

                self.robot.attack(self.dinosaur)
            else:
                break
        self.display_winner()

    def display_winner(self):
        if self.dinosaur.health == 0:
            print(f"{self.robot.name}", "wins")      
        else:
            print(f"{self.dinosaur.name}", "wins") 
