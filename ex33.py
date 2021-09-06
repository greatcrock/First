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

    # def get_damage(self, damage: int):
    #     if self.defense < int(damage):
    #         damage = (int(damage) - self.defense)
    #         self.health -= damage
    #     else:
    #         self.health -= 0


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
        if len(self.units) == 0:
            self.units = [battler() for _ in range(number)]
        else:
            for _ in range(number):
                self.units.append(battler())


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
                print(arm_2.units[0].health)
                if arm_2.units[0].health > 0:
                    arm_2.units[1].heal(arm_2.units[0])
                print(arm_2.units[0].health)
                arm_2.units[1].get_damage(arm_1.units[0].additional_damage)
            if len(arm_2.units) > 1 and arm_2.units[1].health <= 0:
                del arm_2.units[1]
            if arm_2.units[0].health <= 0:
                del arm_2.units[0]
                if len(arm_2.units) == 0:
                    return True
                else:
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
                continue

    # Прямая битва, индекс каждого бойца соответствует индексу бойца из армии напротив.
    # После каждого раунда из команд удаляются мёртвые бойцы.
    def straight_fight(self, army_1, army_2):
        self.arm1, self.arm2 = army_1, army_2
        while True:
            for i in range(min(len(self.arm1.units), len(self.arm2.units))):
                fight(self.arm1.units[i], self.arm2.units[i])
            self.arm1.units = list(filter(lambda x: x.health > 0, self.arm1.units))
            if len(self.arm1.units) == 0:
                return len(self.arm1.units) > len(self.arm2.units)
            self.arm2.units = list(filter(lambda x: x.health > 0, self.arm2.units))
            if len(self.arm2.units) == 0:
                return len(self.arm1.units) > len(self.arm2.units)

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
print("*"*8,type(my_army.units[0]) == Vampire)
my_army.units[0].equip_weapon(weapon_1)
my_army.units[1].equip_weapon(weapon_1)
my_army.units[2].equip_weapon(weapon_2)
enemy_army.units[0].equip_weapon(weapon_1)
enemy_army.units[1].equip_weapon(weapon_2)
enemy_army.units[2].equip_weapon(weapon_2)
battle = Battle()
print(battle.straight_fight(my_army, enemy_army))


weapon_1 = Weapon(-20, 1, 1, 40, -2)
weapon_2 = Weapon(20, 2, 2, -55, 3)
my_army = Army()
my_army.add_units(Vampire, 3)
enemy_army = Army()
enemy_army.add_units(Warrior, 1)
enemy_army.add_units(Defender, 2)
"""
        self.health = int(health)
        self.attack = int(attack)
        self.defense = int(defense)
        self. = int(vampirism) / 10
        self. = int()
"""
a = my_army.units[0].health
b = my_army.units[0].attack
c = my_army.units[0].defense
d = my_army.units[0].vampirism
e = my_army.units[0].heal_power

my_army.units[0].equip_weapon(weapon_1)
print(f"Health {my_army.units[0].health, a}"
      f"\nAttack {my_army.units[0].attack, b}"
      f"\nDefense {my_army.units[0].defense, c}"
      f"\nvampirism {my_army.units[0].vampirism, d}"
      f"\nheal_power {my_army.units[0].heal_power, e}")
my_army.units[1].equip_weapon(weapon_1)
my_army.units[2].equip_weapon(weapon_2)
enemy_army.units[0].equip_weapon(weapon_1)
enemy_army.units[1].equip_weapon(weapon_2)
enemy_army.units[2].equip_weapon(weapon_2)
battle = Battle()
print(battle.straight_fight(my_army, enemy_army))





army_1 = Army()
army_2 = Army()
army_1.add_units(Defender, 11)
army_1.add_units(Vampire, 3)
army_1.add_units(Warrior, 4)
army_2.add_units(Warrior, 4)
army_2.add_units(Defender, 4)
army_2.add_units(Vampire, 13)
battle = Battle()
print("Plese, be True",battle.fight(army_1, army_2))