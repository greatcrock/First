"""
So we have 3 types of units: the Warrior, Knight and Defender. Let's make the battles even more epic and add another type - the Vampire!
Vampire should be the subclass of the Warrior class and have the additional vampirism parameter, which helps him to heal himself.
When the Vampire hits the other unit, he restores his health by +50% of the dealt damage (enemy defense makes the dealt damage value lower).

The basic parameters of the Vampire:
health = 40
attack = 4
vampirism = 50%
You should store vampirism attribute as an integer (50 for 50%). It will be needed to make this solution evolutes to fit one of the next challenges of this saga.
"""


class Warrior:
    # создаёт персонажа с определённым количеством жизней и имющего флаг живого
    def __init__(self):
        self.health = 50
        self.is_alive = True
        self.attack = 5
        self.defense = 0
        self.vampirism = 0

    # отнимает целое число атаки, переданное в него
    def get_damage(self, damage):
        self.health -= int(damage)


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 0.5


class Knight(Warrior):
    # наследует всё от предыдущего класса, но толька атака на 2 больше
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.attack = 7


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.defense = 2
        self.attack = 3

    def get_damage(self, damage: int):
        if self.defense < int(damage):
            damage = (int(damage) - self.defense)
            self.health -= damage
        else:
            pass


def fight(unit_1, unit_2):
    # устравивает битву между персонажами, при чём сначала 1-й атакует 2-го, идёт проверка жив ли  2-й, затем 2-й атакует первого и также идёт проверка
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

rbl = Army()
rbl.add_units(Defender, 1)

vers = Army()
vers.add_units(Vampire, 3)
battle = Battle()
print(battle.fight(rbl, vers))


army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 20)
army_2.add_units(Warrior, 21)
battle = Battle()
print("Faiked",battle.fight(army_1, army_2))