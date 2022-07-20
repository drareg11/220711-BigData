class Player:
        def __init__(self, name, hp, power, lvl):
            self.name = name
            self.hp = hp
            self.power = power
            self.lvl = lvl
            pass
        
        def attack(self):
            return self.power *2
        
        def take_damage(self):
            #Take in amount of damage player should take, subtract that from player health
            pass 

        def changeName(self, name):
            # Change player name to new name. New cannot have ','
            pass
        
        def inc_lvl(self):
            #increase the players level
            pass