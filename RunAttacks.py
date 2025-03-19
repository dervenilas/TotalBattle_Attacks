
import army
import monsters
import captains
import Attacks
import importlib
importlib.reload(army)
importlib.reload(monsters)
importlib.reload(captains)
from army import Army
from monsters import Monsters, Monsters_rare
from captains import Captains
from Attacks import Attack
#### DO NOT MODIFY THE CODE ABOVE THIS LINE ####


bonus_health = 0.
bonus_strength = 0.
monster = Monsters_rare.Undead(6)
troops = [Army.Spearman(3), Army.Rider(3), Army.Archers(3)]  
troops = [Army.Spearman(3), Army.Rider(3)]  
captain = Captains.Aydae(0)


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
attack=Attack(monster, troops, captain, bonus_strength, bonus_health)
attack.attack()