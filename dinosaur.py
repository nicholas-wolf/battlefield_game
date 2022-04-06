import random


class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.attack_power = attack_power

    def attack(self, robot):
        robot.health -= self.attack_power
        print(self.name,"attacks for", self.attack_power, robot.name,"health is now", robot.health)    
