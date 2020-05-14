import random

class Unit:
    def __init__(self, team):
        self.id = random.randint(1, 100)
        self.team = team

class Heroes(Unit):
    def __init__(self, team):
        Unit.__init__(self, team)
        self.level = 0
    
    def lvl_up(self):
        self.level += 10


class Soldiers(Unit):
    def __init__(self, team):
        Unit.__init__(self, team)
    def follow_hero(self, hero):
        print(f'Warrior under ID {self.id} follows the Hero under ID {hero.id}')

warriors1 = []
warriors2 = []

Axe = Heroes(1)
Nirvana = Heroes(2)


for i in range(31):
    n = random.randint(1, 2)
    if n == 1:
        warriors1.append(Soldiers(n))
    elif n == 2:
        warriors2.append(Soldiers(n))

print(f'Team #1: {len(warriors1)} warriors, Team #2: {len(warriors2)} warrriors')

if len(warriors1) > len(warriors2):
    Axe.lvl_up()
    print(f'Axe\'s level has grown up to: {Axe.level}xp')
    warriors1[1].follow_hero(Axe)
else:
    Nirvana.lvl_up()
    print(f'Nirvana\'s level has grown up to: {Nirvana.level}xp')
    warriors1[2].follow_hero(Nirvana)


