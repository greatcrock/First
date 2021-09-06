"""
In this mission you should create a new class Weapon(health, attack, defense, vampirism, heal_power)
which will equip your soldiers with weapons.
Every weapon's object will have the parameters that will show how the soldier's characteristics change while he uses this weapon.
Assume that if the soldier doesn't have some of the characteristics (for example, defense or vampirism), but the weapon have those,
these parameters don't need to be added to the soldier.

The parameters list:
health - add to the current health and the maximum health of the soldier this modificator;
attack - add to the soldier's attack this modificator;
defense - add to the soldier's defense this modificator;
vampirism - increase the soldier’s vampirism to this number (in %. So vampirism = 20 means +20%);
heal_power - increase the amount of health which the healer restore for the allied unit.

All parameters could be positive or negative, so when a negative modificator is being added to the soldier’s stats,
they are decreasing, but none of them can be less than 0.
"""
"""
Input: The warriors, armies and weapons.

Output: The result of the battle (True or False).

How it is used: For computer games development.

Precondition: 5 types of units, 2 types of battles
"""
"""
Also you should create a few standard weapons classes, 
which should be the subclasses of the Weapon. Here’s their list:
Sword - health +5, attack +2
Shield - health +20, attack -1, defense +2
GreatAxe - health -15, attack +5, defense -2, vampirism +10%
Katana - health -20, attack +6, defense -5, vampirism +50%
MagicWand - health +30, attack +3, heal_power +3
"""
# Всё работает хорошо, даже отлично, но надо заменить название переменной army(список, хранит обьекты войнов) на units.
# Этого требуют тесты. См. в ex33.


class Weapon:
    def __init__(self, health=0, attack=0, defense=0, vampirism=0, heal_power=0):
        self.health = int(health)
        self.attack = int(attack)
        self.defense = int(defense)
        self.vampirism = int(vampirism) / 10
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
    def get_damage(self, damage):
        self.health -= int(damage)

    # лечилка, у всех по-умолчанию 0, кроме лекаря
    def heal(self, person):
        person.health += int(self.heal_power) if person.health + self.heal_power <= person.default_health else 0

    def equip_weapon(self, weapon):
        self.health = adder(self.health, weapon.health)
        self.attack = adder(self.attack, weapon.attack)
        self.defense = adder(self.defense, weapon.defense)
        self.vampirism = adder(self.vampirism, weapon.vampirism)
        self.heal_power = adder(self.heal_power, weapon.heal_power)

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

    def get_damage(self, damage: int):
        if self.defense < int(damage):
            damage = (int(damage) - self.defense)
            self.health -= damage
        else:
            self.health -= 0


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
        self.army = []
        self.units = self.army
        # Надо заменить army на units.

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
            arm_1.army[0].health += int(arm_1.army[0].vampirism * (arm_1.army[0].attack - arm_2.army[0].defense if arm_1.army[0].attack - arm_2.army[0].defense > 0 else 0)) if arm_1.army[0].health < 40 else 0
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
            arm_2.army[0].health += int(arm_2.army[0].vampirism *
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


unit_1 = Warrior()
unit_2 = Vampire()
weapon_1 = Weapon(-10, 5, 0, 40, 0)
weapon_2 = Sword()
print(unit_1.attack)
unit_1.equip_weapon(weapon_1)
print(unit_1.attack)
unit_2.equip_weapon(weapon_2)
print(fight(unit_1, unit_2))

weapon_1 = Katana()
weapon_2 = Shield()
my_army = Army()
my_army.add_units(Vampire, 2)
my_army.add_units(Rookie, 2)
enemy_army = Army()
enemy_army.add_units(Warrior, 1)
enemy_army.add_units(Defender, 2)
my_army.units[0].equip_weapon(weapon_1)
my_army.units[1].equip_weapon(weapon_1)
my_army.units[2].equip_weapon(weapon_2)
enemy_army.units[0].equip_weapon(weapon_1)
enemy_army.units[1].equip_weapon(weapon_2)
enemy_army.units[2].equip_weapon(weapon_2)
battle = Battle()
print(battle.straight_fight(my_army, enemy_army))