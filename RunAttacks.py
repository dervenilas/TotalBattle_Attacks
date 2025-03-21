
import army
import monsters
import captains
import Attacks
import importlib
importlib.reload(army)
importlib.reload(monsters)
importlib.reload(captains)
importlib.reload(Attacks)
from army import Army
from monsters import Monsters, Monsters_rare
from captains import Captains
from Attacks import Attack
#### DO NOT MODIFY THE CODE ABOVE THIS LINE ####


bonus_health = 0.4
bonus_strength = 0.25
monster = Monsters.Inferno(10)
troops = [Army.Spearman(3), Army.Rider(3), Army.Archers(3)]  
troops = [Army.Archers(2),Army.Rider(2,450)]  
# troops = [Army.Rider(2,530), Army.Archers(3,740), Army.Archers(2)]  
# troops = [Army.Spearman(3,1600), Army.Battle_Boar(3,10), Army.Rider(3,500)]  
captain = Captains.Alexander(0)


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
attack=Attack(monster, troops, captain, bonus_strength, bonus_health)
attack.attack()