from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = self.choose_weapon()
        
    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(self.name," attacks for ", self.active_weapon.attack_power, dinosaur.name," health is now ", dinosaur.health)    

    def choose_weapon(self):
        weapon_list = [Weapon("sword", 25), Weapon("axe", 15),Weapon("spear", 30)]
        converted_weapon_choice = 1000000
        while converted_weapon_choice <= 0 or converted_weapon_choice >= 2:
            weapon_choice = input("Please choose your weapon: 0 for sword, 1 for axe, 2 for spear ")
            converted_weapon_choice = int(weapon_choice)
            if converted_weapon_choice >= 0 or converted_weapon_choice <= 2:
               return weapon_list[converted_weapon_choice]



