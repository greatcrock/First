"""
A new unit type won’t be added in this mission, but instead we’ll add a new tactic - straight_fight(army_1, army_2).
It should be the method of the Battle class and it should work as follows:
at the beginning there will be a few duels between each pair of soldiers from both armies (the first unit against the first, the second against the second and so on).
After that all dead soldiers will be removed and the process repeats until all soldiers of one of the armies will be dead.
Armies might not have the same number of soldiers.
If a warrior doesn’t have an opponent from the enemy army - we’ll automatically assume that he’s won a duel
(for example - 9th and 10th units from the first army, if the second has only 8 soldiers).

Input: The warriors and armies.
Output: The result of the battle (True or False).

Precondition: 5 types of units, 2 types of battles
"""


# основной класс бойца
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
        person.health += int(self.heal_points) if person.health + self.heal_points <= person.default_health else 0


# доктор
class Healer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 0
        self.health = 60
        self.heal_points = 2
        self.default_health = 60


# копейщик
class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 6
        self.additional_damage = 3


# вампир
class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 0.5
        self.default_health = 40


# рыцарь
class Knight(Warrior):
    # наследует всё от предыдущего класса, но толька атака на 2 больше
    def __init__(self):
        super().__init__()
        self.attack = 7


# защитник
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
            self.health -= 0


# битва между бойцами:
def fight(unit_1, unit_2):
    while unit_1.health > 0 and unit_2.health > 0:
        unit_2.health -= (unit_1.attack - unit_2.defense if unit_1.attack - unit_2.defense > 0 else 0)
        unit_1.health += unit_1.vampirism * (unit_1.attack - unit_2.defense if unit_1.attack - unit_2.defense > 0 else 0)
        if unit_2.health <= 0:
            unit_2.is_alive = False
            break
        unit_1.health -= (unit_2.attack - unit_1.defense if unit_2.attack - unit_1.defense > 0 else 0)
        unit_2.health += unit_2.vampirism * (unit_2.attack - unit_1.defense if unit_2.attack - unit_1.defense > 0 else 0)
        if unit_1.health <= 0:
            unit_1.is_alive = False
            break
    return unit_1.health > unit_2.health


# Армия
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


# класс битвы
class Battle:

    # устраивает битву между двумя войсками (списками свойнами из прошлого класса)
    def fight(self, arm_1, arm_2):
        while True:
            # блок кода, где армия № 1 бьёт армию № 2
            arm_2.army[0].get_damage(arm_1.army[0].attack)
            # Вампирский дополнительный навык
            arm_1.army[0].health += arm_1.army[0].vampirism * (arm_1.army[0].attack - arm_2.army[0].defense if arm_1.army[0].attack - arm_2.army[0].defense else 0) if arm_1.army[0].health < 40 else 0
            if len(arm_2.army) >= 2:
                print(arm_2.army[0].health)
                if arm_2.army[0].health > 0:
                    arm_2.army[1].heal(arm_2.army[0])
                print(arm_2.army[0].health)
                arm_2.army[1].get_damage(arm_1.army[0].additional_damage)
            if len(arm_2.army) > 1 and arm_2.army[1].health <= 0:
                del arm_2.army[1]
            if arm_2.army[0].health <= 0:
                del arm_2.army[0]
                if len(arm_2.army) == 0:
                    return True
                else:
                    continue

            # блок кода, где армия № 2 бьёт армию № 1
            arm_1.army[0].get_damage(arm_2.army[0].attack)
            arm_2.army[0].health += (arm_2.army[0].vampirism *
                                     (arm_2.army[0].attack - arm_1.army[0].defense if arm_2.army[0].attack - arm_1.army[0].defense > 0 else 0)) if arm_2.army[0].health < 40 else 0
            if len(arm_1.army) > 1:
                if arm_1.army[0].health > 0:
                    arm_1.army[1].heal(arm_1.army[0])
                arm_1.army[1].get_damage(arm_2.army[0].additional_damage)
            if len(arm_1.army) > 1 and arm_1.army[1].health <= 0:
                del arm_1.army[1]
            if arm_1.army[0].health <= 0:
                del arm_1.army[0]
                if len(arm_1.army) == 0:
                    return False
                continue

    # Прямая битва, индекс каждого бойца соответствует индексу бойца из армии напротив.
    # После каждого раунда из команд удаляются мёртвые бойцы.
    def straight_fight(self, army_1, army_2):
        self.arm1, self.arm2 = army_1, army_2
        while True:
            for i in range(min(len(self.arm1.army), len(self.arm2.army))):
                fight(self.arm1.army[i], self.arm2.army[i])
            self.arm1.army = list(filter(lambda x: x.health > 0, self.arm1.army))
            if len(self.arm1.army) == 0:
                return len(self.arm1.army) > len(self.arm2.army)
            self.arm2.army = list(filter(lambda x: x.health > 0, self.arm2.army))
            if len(self.arm2.army) == 0:
                return len(self.arm1.army) > len(self.arm2.army)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False