"""
In this mission you should add a new class Warlord(), which should be the subclass of the Warrior class and have the
next characteristics:
health = 100
attack = 4
defense = 2

Also, when the Warlord is included in any of the armies, that particular army gets the new move_units() method which
allows to rearrange the units of that army for the better battle result.
The rearrangement is done not only before the battle, but during the battle too, each time the allied units die.
The rules for the rearrangement are as follow:
1) If there are Lancers in the army, they should be placed in front of everyone else.
2) If there is a Healer in the army, he should be placed right after the first soldier to heal him during the fight.
    If the number of Healers is > 1, all of them should be placed right behind the first Healer.
3) If there are no more Lancers in the army, but there are other soldiers who can deal damage,
they also should be placed in first position, and the Healer should stay in the 2nd row (if army still has Healers).
4) Warlord should always stay way in the back to look over the battle and rearrange the soldiers when it's needed.
5) Every army can have no more than 1 Warlord.
6) If the army doesn’t have a Warlord, it can’t use the move_units() method.
"""

class Weapon:
    def __init__(self, health=0, attack=0, defense=0, vampirism=0, heal_power=0):
        self.health = int(health)
        self.attack = int(attack)
        self.defense = int(defense)
        self.vampirism = int(vampirism) / 100
        self.heal_power = int(heal_power)


class Sword(Weapon):
    def __init__(self):
        super().__init__()
        self.health = 5
        self.attack = 2


class Shield(Weapon):
    def __init__(self):
        super().__init__()
        self.health = 20
        self.attack = -1
        self.defense = 2


class GreatAxe(Weapon):
    def __init__(self):
        super().__init__()
        self.attack = 5
        self.health = -15
        self.defense = -2
        self.vampirism = 0.1


class Katana(Weapon):
    def __init__(self):
        super().__init__()
        self.health = -20
        self.attack = 6
        self.defense = -5
        self.vampirism = 0.5


class MagicWand(Weapon):
    def __init__(self):
        super().__init__()
        self.health = 30
        self.attack = 3
        self.heal_power = 3


# Функция, которая складывает умения аттрибутов класса война и оружия
def adder(unit1, unit2):
    if float(unit1) + float(unit2) > 0 and unit1 > 0:
        return float(unit1) + float(unit2)
    else:
        return 0


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
        self.heal_power = 0
        self.default_health = 50

    # отнимает целое число атаки, переданное в него
    def get_damage(self, damage: int):
        if self.defense < int(damage):
            damage = (int(damage) - self.defense)
            self.health -= damage
        else:
            self.health -= 0

    # лечилка, у всех по-умолчанию 0, кроме лекаря
    def heal(self, person):
        person.health += int(self.heal_power) if person.health + self.heal_power <= person.default_health else 0

    def equip_weapon(self, weapon):
        self.health = adder(self.health, weapon.health)
        self.attack = adder(self.attack, weapon.attack)
        self.defense = adder(self.defense, weapon.defense)
        self.vampirism = adder(self.vampirism, weapon.vampirism)
        self.heal_power = adder(self.heal_power, weapon.heal_power)

class Warlord(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.default_health = 100
        self.attack = 4
        self.defense = 2

# доктор
class Healer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 0
        self.health = 60
        self.heal_power = 2
        self.default_health = 60


# копейщик
class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 6
        self.additional_damage = int(self.attack) * 0.5


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


class Rookie(Warrior):
    def __init__(self):
        super().__init__()
        self.max_health = 50
        self.default_health = 50
        self.attack = 1


# битва между бойцами:
def fight(unit_1, unit_2):
    while unit_1.health > 0 and unit_2.health > 0:
        unit_2.health -= (unit_1.attack - unit_2.defense if unit_1.attack - unit_2.defense > 0 else 0)
        unit_1.health += int(unit_1.vampirism * (unit_1.attack - unit_2.defense) if unit_1.attack - unit_2.defense > 0 else 0)
        if unit_2.health <= 0:
            unit_2.is_alive = False
            break
        unit_1.health -= (unit_2.attack - unit_1.defense if unit_2.attack - unit_1.defense > 0 else 0)
        unit_2.health += int(unit_2.vampirism * (unit_2.attack - unit_1.defense) if unit_2.attack - unit_1.defense > 0 else 0)
        if unit_1.health <= 0:
            unit_1.is_alive = False
            break
    return unit_1.health > unit_2.health


# Армия
class Army:
    def __init__(self):
        self.units = []

    # создаёт список с пресонажами Одного Типа (Только рыцари либо только войны)
    def add_units(self, warrior_class, number):
        battler = warrior_class
        if warrior_class == Warlord:
            number = 1
        if Warlord in self.units:
            number = 0
        if len(self.units) == 0:
            self.units = [battler() for _ in range(number)]
        else:
            for _ in range(number):
                self.units.append(battler())

    def move_units(self):
        warlord = [u for u in self.units if isinstance(u, Warlord)]
        if not warlord:
            return

        lancers = [u for u in self.units if isinstance(u, Lancer)]
        other_attackers = [u for u in self.units if u.attack > 0 and not isinstance(u, Lancer) and not isinstance(u, Warlord)]
        healers = [u for u in self.units if isinstance(u, Healer)]

        lineup = lancers + other_attackers
        lineup2 = lineup[:1] + healers + lineup[1:]

        self.units = lineup2 + warlord

    def cleanup(self):
        front_warrior_dead = self.units and not self.units[0].is_alive
        self.units = [u for u in self.units if u.is_alive]
        return front_warrior_dead

    def all_dead(self):
        return self.units == []



# класс битвы
class Battle:
    # устраивает битву между двумя войсками (списками свойнами из прошлого класса)
    def fight(self, arm_1, arm_2):
        while True:
            # блок кода, где армия № 1 бьёт армию № 2
            arm_2.units[0].get_damage(arm_1.units[0].attack)
            # Вампирский дополнительный навык
            arm_1.units[0].health += int(arm_1.units[0].vampirism * (arm_1.units[0].attack - arm_2.units[0].defense if arm_1.units[0].attack - arm_2.units[0].defense > 0 else 0)) if arm_1.units[0].health < 40 else 0
            if len(arm_2.units) >= 2:

                if arm_2.units[0].health > 0:
                    arm_2.units[1].heal(arm_2.units[0])
                arm_2.units[1].get_damage(arm_1.units[0].additional_damage)
            if len(arm_2.units) > 1 and arm_2.units[1].health <= 0:
                del arm_2.units[1]
            if arm_2.units[0].health <= 0:
                del arm_2.units[0]
                if len(arm_2.units) == 0:
                    return True
                else:
                    if len([i for i in arm_2.units if type(i) == Warlord]) > 0:
                        arm_2.move_units()
                    continue

            # блок кода, где армия № 2 бьёт армию № 1
            arm_1.units[0].get_damage(arm_2.units[0].attack)
            arm_2.units[0].health += int(arm_2.units[0].vampirism *
                                     (arm_2.units[0].attack - arm_1.units[0].defense if arm_2.units[0].attack - arm_1.units[0].defense > 0 else 0)) if arm_2.units[0].health < 40 else 0
            if len(arm_1.units) > 1:
                if arm_1.units[0].health > 0:
                    arm_1.units[1].heal(arm_1.units[0])
                arm_1.units[1].get_damage(arm_2.units[0].additional_damage)
            if len(arm_1.units) > 1 and arm_1.units[1].health <= 0:
                del arm_1.units[1]
            if arm_1.units[0].health <= 0:
                del arm_1.units[0]
                if len(arm_1.units) == 0:
                    return False
                if len([i for i in arm_1.units if type(i) == Warlord]) > 0:
                    arm_1.move_units()
                continue

    # Прямая битва, индекс каждого бойца соответствует индексу бойца из армии напротив.
    # После каждого раунда из команд удаляются мёртвые бойцы.
    def straight_fight(self, army_1, army_2):
        self.arm1, self.arm2 = army_1, army_2
        while not self.arm1.all_dead() and not self.arm2.all_dead():
            for u1, u2 in zip(self.arm1.units, self.arm2.units):
                fight(u1, u2)
            self.arm1.cleanup()
            self.arm2.cleanup()
        return self.arm2.all_dead()
            # for u1, u2 in zip(self.arm1.units, self.arm2.units):
            #     fight(u1, u2)
            # self.arm1.units = [i for i in self.arm1.units if i.is_alive]
            # self.arm1.move_units()
            # if len(self.arm1.units) == 0:
            #     return len(self.arm1.units) > len(self.arm2.units)
            # # self.arm2.units = list(filter(lambda x: x.health > 0, self.arm2.units))
            # self.arm2.units = [i for i in self.arm2.units if i.is_alive]
            # if len(self.arm2.units) == 0:
            #     return len(self.arm1.units) > len(self.arm2.units)



#
# ronald = Warlord()
# heimdall = Knight()
#
# print(fight(heimdall, ronald) == False)
#
# my_army = Army()
# my_army.add_units(Warlord, 1)
# my_army.add_units(Warrior, 2)
# my_army.add_units(Lancer, 2)
# my_army.add_units(Healer, 2)
#
# enemy_army = Army()
# enemy_army.add_units(Warlord, 3)
# enemy_army.add_units(Vampire, 1)
# enemy_army.add_units(Healer, 2)
# enemy_army.add_units(Knight, 2)
#
# my_army.move_units()
# enemy_army.move_units()
#
# print("Lancer good",type(my_army.units[0]) == Lancer)
# print("Healer the second",type(my_army.units[1]) == Healer)
# print("Warlord the last",type(my_army.units[-1]) == Warlord)
#
# print("Vampyre is the firtst",type(enemy_army.units[0]) == Vampire)
# print(enemy_army.units[0].attack)
# print(enemy_army.units[5].attack)
# print(enemy_army.units[0])
# print(type(enemy_army.units[-1]) == Warlord)
# print(type(enemy_army.units[-2]) == Knight)
#
# #6, not 8, because only 1 Warlord per army could be
# print("Test", len(enemy_army.units) == 6)
# print(len(enemy_army.units))
# print(enemy_army.units)
#
# battle = Battle()
#
# print(battle.fight(my_army, enemy_army) == True)

# army_1 = Army()
# army_2 = Army()
# army_1.add_units(Warlord, 1)
# army_1.add_units(Warrior, 2)
# army_1.add_units(Lancer, 2)
# army_1.add_units(Healer, 2)
#
# army_2.add_units(Warlord, 1)
# army_2.add_units(Vampire, 1)
# army_2.add_units(Healer, 2)
# army_2.add_units(Knight, 2)
#
#
# army_1.move_units()
#
# army_2.move_units()
# print("Army1", *army_1.units)
# print("Army2", *army_2.units)
# battle = Battle()
# print(battle.fight(army_1,army_2))
#
#
#
# army_1 = Army()
# army_2 = Army()
# army_1.add_units(Defender, 11)
# army_1.add_units(Vampire, 3)
# army_1.add_units(Warrior, 4)
# army_2.add_units(Warrior, 4)
# army_2.add_units(Defender, 4)
# army_2.add_units(Vampire, 13)
# battle = Battle()
# print(battle.fight(army_1, army_2))
#
#
# army_1 = Army()
# army_2 = Army()
# army_1.add_units(Warrior, 2)
# army_1.add_units(Lancer, 2)
# army_1.add_units(Defender, 1)
# army_1.add_units(Warlord, 3)
# army_2.add_units(Warlord, 2)
# army_2.add_units(Vampire, 1)
# army_2.add_units(Healer, 5)
# army_2.add_units(Knight, 2)
# army_1.move_units()
# army_2.move_units()
# battle = Battle()
# print(battle.fight(army_1, army_2))


army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 2)
army_1.add_units(Lancer, 3)
army_1.add_units(Defender, 1)
army_1.add_units(Warlord, 1)
army_2.add_units(Warlord, 5)
army_2.add_units(Vampire, 1)
army_2.add_units(Rookie, 1)
army_2.add_units(Knight, 1)
army_1.units[0].equip_weapon(Sword())
army_2.units[0].equip_weapon(Shield())
army_1.move_units()
army_2.move_units()
battle = Battle()
print(battle.straight_fight(army_1, army_2))
