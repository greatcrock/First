"""
The battle continues and each army is losing good warriors.
Let's try to fix that and add a new unit type - the Healer.
Healer won't be fighting (his attack = 0, so he can't deal the damage).
But his role is also very important - every time the allied soldier hits
the enemy, the Healer will heal the allie, standing right in front of him
by +2 health points with the heal() method.
Note that the health after healing can't be greater than the maximum health of the unit.
For example, if the Healer heals the Warrior with 49 health points,
the Warrior will have 50 hp, because this is the maximum for him.
The basic parameters of the Healer:
health = 60
attack = 0

"""


class Warrior:
    # создаёт персонажа с определённым количеством жизней и имющего флаг живого
    def __init__(self):
        self.health = 50
        self.is_alive = True if self.health > 0 else False
        self.attack = 5
        self.defense = 0
        self.vampirism = 0
        self.additional_damage = 0
        self.heal_points = 0
        self.default_health = 50

    # отнимает целое число атаки, переданное в него
    def get_damage(self, damage):
        self.health -= int(damage)

    # лечилка, у всех по-умолчанию 0, кроме лекаря
    def heal(self, person):
        print("Health before", person.health)
        person.health += int(self.heal_points) if person.health + self.heal_points <= person.default_health else 0
        print("Health after", person.health)
            #


class Healer(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.heal_points = 2
        self.default_health = 60


class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 6
        self.additional_damage = 3


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 0.5
        self.default_health = 40


class Knight(Warrior):
    # наследует всё от предыдущего класса, но толька атака на 2 больше
    def __init__(self):
        super().__init__()
        self.attack = 7


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.defense = 2
        self.attack = 3
        self.default_health = 60

    def get_damage(self, damage: int):
        if self.defense < int(damage):
            damage = (int(damage) - self.defense)
            self.health -= damage
        else:
            pass


def fight(unit_1, unit_2):
    # устравивает битву между персонажами, при чём
    # сначала 1-й атакует 2-го, идёт проверка жив ли 2-й, затем 2-й атакует первого и также идёт проверка
    while unit_1.health > 0 and unit_2.health > 0:
        unit_2.get_damage(unit_1.attack)
        unit_1.health += unit_1.vampirism * (unit_1.attack - unit_2.defense if unit_2.defense < unit_1.attack else 0) if unit_2.health < 40 else 0
        if unit_2.health <= 0:
            unit_2.is_alive = False
            break
        unit_1.get_damage(unit_2.attack)
        unit_2.health += (unit_1.vampirism * (unit_2.attack - unit_1.defense if unit_1.defense < unit_2.attack else 0)) if unit_2.health < 40 else 0
        if unit_1.health <= 0:
            unit_1.is_alive = False
            break
    # возвращает результат битвы: если победил 1-й то True, в ином случае False. Побеждает строго 1 персонаж (нет ничьих)
    return unit_1.health > 0 and unit_2.health <= 0


class Army:
    def __init__(self):
        self.army = []

    # создаёт список с пресонажами Одного Типа (Только рыцари либо только войны)
    def add_units(self, warrior_class, number):
        battler = warrior_class
        if len(self.army) == 0:
            self.army = [battler() for _ in range(number)]
        else:
            for _ in range(number):
                self.army.append(battler())


class Battle:
    # устраивает битву между двумя войсками (списками свойнами из прошлого класса)
    def fight(self, arm_1, arm_2):
        self.army_1 = arm_1
        self.army_2 = arm_2
        while True:
            unit_1 = self.army_1.army[0]
            unit_2 = self.army_2.army[0]

            # блок кода, где армия № 1 бьёт армию № 2
            self.army_2.army[0].get_damage(self.army_1.army[0].attack)
            if len(self.army_2.army) > 1:
                self.army_2.army[1].heal(self.army_2.army[0])
                self.army_2.army[1].get_damage(unit_1.additional_damage)
            # Вампирский дополнительный навык
            unit_1.health += unit_1.vampirism * (unit_1.attack - unit_2.defense if unit_2.defense < unit_1.attack else 0) if unit_2.health < 40 else 0
            if len(self.army_2.army) > 1 and self.army_2.army[1].health <= 0:
                del self.army_2.army[1]
            if self.army_2.army[0].health <= 0:
                del self.army_2.army[0]
                if len(self.army_2.army) == 0:
                    return len(self.army_1.army) > len(self.army_2.army)
                continue

            # блок кода, где армия № 2 бьёт армию № 1
            unit_1.get_damage(self.army_2.army[0].attack)
            if len(self.army_1.army) > 1:
                self.army_1.army[1].heal(self.army_1.army[0])
                self.army_1.army[1].get_damage(self.army_2.army[0].additional_damage)
            self.army_2.army[0].health += (unit_1.vampirism *
                                           (self.army_2.army[0].attack - unit_1.defense if unit_1.defense < self.army_2.army[0].attack else 0)) if self.army_2.army[0].health < 40 else 0
            if len(self.army_1.army) > 1 and self.army_1.army[1].health <= 0:
                del self.army_1.army[1]
            if self.army_1.army[0].health <= 0:
                del self.army_1.army[0]
                if len(self.army_1.army) == 0:
                    return len(self.army_1.army) > len(self.army_2.army)
                continue


chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()
bob = Defender()
mike = Knight()
rog = Warrior()
lancelot = Defender()
eric = Vampire()
adam = Vampire()
richard = Defender()
ogre = Warrior()
freelancer = Lancer()
vampire = Vampire()

print(fight(chuck, bruce) == True,
fight(dave, carl) == False,
chuck.is_alive == True,
bruce.is_alive == False,
carl.is_alive == True,
dave.is_alive == False,
fight(carl, mark) == False,
carl.is_alive == False,
fight(bob, mike) == False,
fight(lancelot, rog) == True,
fight(eric, richard) == False,
fight(ogre, adam) == True,
fight(freelancer, vampire) == True,
freelancer.is_alive == True,
      sep="\n")

my_army = Army()
my_army.add_units(Defender, 2)
my_army.add_units(Vampire, 2)
my_army.add_units(Lancer, 4)
my_army.add_units(Warrior, 1)

enemy_army = Army()
enemy_army.add_units(Warrior, 2)
enemy_army.add_units(Lancer, 2)
enemy_army.add_units(Defender, 2)
enemy_army.add_units(Vampire, 3)

army_3 = Army()
army_3.add_units(Warrior, 1)
army_3.add_units(Lancer, 1)
army_3.add_units(Defender, 2)

army_4 = Army()
army_4.add_units(Vampire, 3)
army_4.add_units(Warrior, 1)
army_4.add_units(Lancer, 2)

battle = Battle()
print("New")
print(battle.fight(my_army, enemy_army))
print(battle.fight(army_3, army_4))

army_5 = Army()
army_5.add_units(Warrior, 12)

army_6 = Army()
army_6.add_units(Warrior, 11)

print(battle.fight(army_5, army_6))

army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 20)
army_2.add_units(Warrior, 21)
battle = Battle()
print(battle.fight(army_1, army_2))

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()
    priest = Healer()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True
    # assert freelancer.health == 14
    # priest.heal(freelancer)
    # assert freelancer.health == 16

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 4)
    enemy_army.add_units(Healer, 1)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)
    enemy_army.add_units(Healer, 1)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Healer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Healer, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 4)
    enemy_army.add_units(Healer, 1)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)
    enemy_army.add_units(Healer, 1)

army_3 = Army()
army_3.add_units(Warrior, 1)
army_3.add_units(Lancer, 1)
army_3.add_units(Healer, 1)
army_3.add_units(Defender, 2)

army_4 = Army()
army_4.add_units(Vampire, 3)
army_4.add_units(Warrior, 1)
army_4.add_units(Healer, 1)
army_4.add_units(Lancer, 2)

battle = Battle()

print(battle.fight(my_army, enemy_army) == False )
print(battle.fight(army_3, army_4) == True)


doctor = Healer()
ceff = Warrior()
jim = Knight()
print(jim.health)
fight(jim, ceff)
print(jim.health)
doctor.heal(jim)
print(jim.health)