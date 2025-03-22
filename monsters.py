import copy

class Monster_units:
    
    class Axe_Thrower:
        def __init__(self, amount = 1):
            self.type = ["Barbarian", "Ranged"] 
            self.strength = 360
            self.health = 1080
            self.bonus = [["Melee", 0.45],["Flying", 0.50]]
            self.amount = amount
    
    class Banshee:
        def __init__(self, amount = 1):
            self.type = ["Undead", "Ranged"]
            self.strength = 100
            self.health = 300
            self.bonus = [["Melee", 0.45]]
            self.amount = amount
            
    class Dark_Rider:
        def __init__(self, amount = 1):
            self.type = ["Undead", "Mounted"]
            self.strength = 5800
            self.health = 17400
            self.bonus = [["Ranged", 0.50]]
            self.amount = amount
            
    class Deathhound_Rider:
        def __init__(self, amount = 1):
            self.type = ["Undead", "Mounted"]
            self.strength = 1100
            self.health = 3300
            self.bonus = [["Ranged", 0.40]]
            self.amount = amount

    class Dwarf:
        def __init__(self, amount = 1):
            self.type = ["Elves", "Melee"]
            self.strength = 28
            self.health = 84
            self.bonus = [["Mounted", 0.1]]
            self.amount = amount
    
    class Elven_Archer:
        def __init__(self, amount = 1):
            self.type = ["Elves", "Ranged"]
            self.strength = 100
            self.health = 300
            self.bonus = [["Melee", 0.35]]
            self.amount = amount

    class Fiend:
        def __init__(self, amount = 1):
            self.type = ["Demon", "Melee"]
            self.strength = 28
            self.health = 84
            self.bonus = [["Mounted", 0.15]]
            self.amount = amount

    class Ghoul:
        def __init__(self, amount = 1):
            self.type = ["Beast","Undead", "Melee"]
            self.strength = 28
            self.health = 84
            self.bonus = [["Mounted", 0.10]]
            self.amount = amount

    class Goblin:
        def __init__(self, amount = 1):
            self.type = ["Barbarian", "Melee"]
            self.strength = 28
            self.health = 84
            self.bonus = [["Mounted", 0.10]]
            self.amount = amount
            
    class Jaguar_Rider:
        def __init__(self, amount = 1):
            self.type = ["Cursed", "Mounted"]
            self.strength = 270
            self.health = 810
            self.bonus = [["Ranged", 0.30]]
            self.amount = amount

    class Magog:
        def __init__(self, amount = 1):
            self.type = ["Demon", "Ranged"]
            self.strength = 50
            self.health = 150
            self.bonus = [["Melee", 0.30]]
            self.amount = amount
            
    class Necromancer:
        def __init__(self, amount = 1):
            self.type = ["Undead", "Ranged"]
            self.strength = 720
            self.health = 2160
            self.bonus = [["Melee", 0.50]]
            self.amount = amount
            
    class Ogre_Shaman:
        def __init__(self, amount = 1):
            self.type = ["Barbarian", "Melee"]
            self.strength = 3200
            self.health = 9600
            self.bonus = [["Mounted", 0.6]]
            self.amount = amount
            
    class Overseer:
        def __init__(self, amount = 1):
            self.type = ["Demon", "Ranged"]
            self.strength = 6500
            self.health = 19500
            self.bonus = [["Melee", 0.70]]
            self.amount = amount
            
    class Skeleton:
        def __init__(self, amount = 1):
            self.type = ["Cursed", "Melee"]
            self.strength = 56
            self.health = 168
            self.bonus = [["Mounted", 0.15]]
            self.amount = amount
            
    class Storm_Crow:
        def __init__(self, amount = 1):
            self.type = ["Barbarian", "Flying", "Beast"]
            self.strength = 13000
            self.health = 39000
            self.bonus = [["Melee", 0.55],["Elemental", 0.45]]
            self.amount = amount
    
    class Withch_Doctor:
        def __init__(self, amount = 1):
            self.type = ["Cursed", "Ranged"]
            self.strength = 150
            self.health = 450
            self.bonus = [["Melee", 0.25]]
            self.amount = amount

    class Wolf_Rider:
        def __init__(self, amount = 1):
            self.type = ["Barbarian", "Mounted"]
            self.strength = 150
            self.health = 450
            self.bonus = [["Ranged", 0.6],[ "Siege", 0.4]]
            self.amount = amount

class Monsters:

    class Barbarian:
        level_data = {
             4:  [Monster_units.Goblin(330)],
             9:  [Monster_units.Wolf_Rider(510)],
            12:  [Monster_units.Wolf_Rider(1200), Monster_units.Goblin(2800)],
        }

        def __init__(self, level):
            self.level = level
            if level in self.level_data:
                self.units = copy.deepcopy(self.level_data[level])
            else:
                raise ValueError(f"Invalid level {level} for Barbarian.")

    class Cursed:
        level_data = {
            8:  [Monster_units.Withch_Doctor(330)],
            12: [Monster_units.Skeleton(1100), Monster_units.Jaguar_Rider(550)],
        }
        
        def __init__(self, level):
            self.level = level
            if level in self.level_data:
                self.units = copy.deepcopy(self.level_data[level])
            else:
                raise ValueError(f"Invalid level {level} for Cursed.")
            
    class Elf:
        level_data = {
            2:  [Monster_units.Dwarf(700)],
            7:  [Monster_units.Elven_Archer(300)],
            11: [Monster_units.Elven_Archer(1200), Monster_units.Dwarf(1900)],
        }
        
        def __init__(self, level):
            self.level = level
            if level in self.level_data:
                self.units = copy.deepcopy(self.level_data[level])
            else:
                raise ValueError(f"Invalid level {level} for Elf.")
    
    class Inferno:
        level_data = {
            5:  [Monster_units.Fiend(500)],
            10: [Monster_units.Magog(2300)],
        }

        def __init__(self, level):
            self.level = level
            if level in self.level_data:
                self.units = copy.deepcopy(self.level_data[level])
            else:
                raise ValueError(f"Invalid level {level} for Inferno.")

    class Undead:
        level_data = {
            1:  [Monster_units.Ghoul(93)],
            6:  [Monster_units.Banshee(210)],
            12: [Monster_units.Ghoul(1500), Monster_units.Deathhound_Rider(91)],
            13: [Monster_units.Deathhound_Rider(110), Monster_units.Necromancer(380)],
                        
        }
        
        def __init__(self, level):
            self.level = level
            if level in self.level_data:
                self.units = copy.deepcopy(self.level_data[level])
            else:
                raise ValueError(f"Invalid level {level} for Undead.")

class Monsters_rare:

    class Barbarian:
        level_data = {
            4: [Monster_units.Ogre_Shaman(4), Monster_units.Wolf_Rider(39), Monster_units.Goblin(70)],
            9: [Monster_units.Storm_Crow(6), Monster_units.Wolf_Rider(360), Monster_units.Axe_Thrower(150)],
        }

        def __init__(self, level):
            self.level = level
            if level in self.level_data:
                self.units = copy.deepcopy(self.level_data[level])
            else:
                raise ValueError(f"Invalid level {level} for Barbarian.")

    class Cursed:
        level_data = {
            0:  [Monster_units.Withch_Doctor(330)],
        }
        
        def __init__(self):
            self.level = level
            if level in self.level_data:
                self.units = copy.deepcopy(self.level_data[level])
            else:
                raise ValueError(f"Invalid level {level} for Cursed.")
            
    class Elf:
        level_data = {
            0:  [Monster_units.Dwarf(700)],
        }
        
        def __init__(self, level):
            self.level = level
            if level in self.level_data:
                self.units = copy.deepcopy(self.level_data[level])
            else:
                raise ValueError(f"Invalid level {level} for Elf.")
    
    class Inferno:
        level_data = {
            5:  [Monster_units.Fiend(110), Monster_units.Magog(180), Monster_units.Overseer(3)],
        }

        def __init__(self, level):
            self.level = level
            if level in self.level_data:
                self.units = copy.deepcopy(self.level_data[level])
            else:
                raise ValueError(f"Invalid level {level} for Inferno.")

    class Undead:
        level_data = {
            1:  [Monster_units.Banshee(16), Monster_units.Ghoul(56), Monster_units.Deathhound_Rider(2)],
            6:  [Monster_units.Banshee(48), Monster_units.Dark_Rider(5), Monster_units.Deathhound_Rider(13)],
        }
        
        def __init__(self, level):
            self.level = level
            if level in self.level_data:
                self.units = copy.deepcopy(self.level_data[level])
            else:
                raise ValueError(f"Invalid level {level} for Undead.")
