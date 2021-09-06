"""
In the previous mission - Army battles, you've learned how to make a battle between 2 armies.
But we have only 2 types of units - the Warriors and Knights. Let's add another one - the Defender.
It should be the subclass of the Warrior class and have an additional defense parameter, which helps him to survive longer.
When another unit hits the defender, he loses a certain amount of his health according to the next formula:
enemy attack - self defense (if enemy attack > self defense). Otherwise, the defender doesn't lose his health.
The basic parameters of the Defender:
health = 60
attack = 3
defense = 2
"""
"""
Input: The warriors and armies.

Output: The result of the battle (True or False).

How it is used: For the computer games development.

Note: From now on, the tests from "check" part will use another type of warrior: the rookie. Its code is

class Rookie(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.health = 50
        self.attack = 1

Precondition: 3 types of units
"""
class Warrior:
    # создаёт персонажа с определённым количеством жизней и имющего флаг живого
    def __init__(self):
        self.health = 50
        self.is_alive = True
        self.attack = 5


    # отнимает целое число атаки, переданное в него
    def get_damage(self, damage):
        self.health -= int(damage)

class Knight(Warrior):
    # наследует всё от предыдущего класса, но толька атака на 2 больше
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.attack = 7

"""
enemy attack - self defense (if enemy attack > self defense). Otherwise, the defender doesn't lose his health.
The basic parameters of the Defender:
health = 60
attack = 3
defense = 2
"""
class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.defense = 2
        self.attack = 3


    def get_damage(self, damage:int):
        if self.defense < int(damage):
            self.health -= (int(damage) - self.defense)
        else:
            pass

            
            
def fight(unit_1, unit_2):
    # устравивает битву между персонажами, при чём сначала 1-й атакует 2-го, идёт проверка жив ли  2-й, затем 2-й атакует первого и также идёт проверка
    while unit_1.health > 0 and unit_2.health > 0:
        unit_2.get_damage(unit_1.attack)
        if unit_2.health <= 0:
            unit_2.is_alive = False
            break
        unit_1.get_damage(unit_2.attack)
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
        # бксконечный цикл, идёт пока его не остановят изнутри
        while True:
            # оценивает результат битвы между войнами по индексом 0. Если победил 1-й, то вычёркивает 2-го из списка его армии
            if fight(self.army_1.army[0], self.army_2.army[0]):
                print("Army 2 lost")
                del self.army_2.army[0]
                if len(self.army_2.army) == 0:
                    break
            # если победил воторой, то вычёркивает первого из списка его армии
            else:
                print("Army 1 lost")
                del self.army_1.army[0]
                if len(self.army_1.army) == 0:
                    break
        # Война идёт до победного, и если в первой армии осталось больше бойцов, то возвращает True, в обратном случае False
        return len(self.army_1.army) > len(self.army_2.army)


# my_army = Army()
# my_army.add_units(Knight, 1)
# print(my_army.army)
# enemy_army = Army()
# enemy_army.add_units(Warrior, 1)
# print(enemy_army.army)
battle = Battle()
# print(battle.fight(my_army, enemy_army))
# army_3 = Army()
# army_3.add_units(Warrior, 1)
# army_3.add_units(Defender, 1)
# print("Army-3",*army_3.army)
# army_4 = Army()
# army_4.add_units(Warrior, 2)
# print("Army-4", *army_4.army)
# print(battle.fight( army_4,army_3))
#
# army_1 = Army()
# army_1.add_units(Warrior, 3)
# army_2 = Army()
# army_2.add_units(Warrior, 1)
# print(1,battle.fight(army_1,army_2))
# print(army_2.army, army_1.army)
# army_1 = Army()
# army_2 = Army()
# army_1.add_units(Warrior, 1)
# army_2.add_units(Warrior, 2)
# print("2",battle.fight( army_1,army_2))

rbl = Army()
rbl.add_units(Defender, 1)

vers = Army()
vers.add_units(Warrior, 2)

print(battle.fight(rbl, vers))