ATTRS = ['health', 'attack', 'defense', 'vampirism', 'heal_power']

class Weapon:
    def __init__(self, health, attack, defense, vampirism, heal_power):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.vampirism = vampirism
        self.heal_power = heal_power

class Sword(Weapon):
    def __init__(self):
        super().__init__(5, 2, None, None, None)

class Shield(Weapon):
    def __init__(self):
        super().__init__(20, -1, 2, None, None)

class GreatAxe(Weapon):
    def __init__(self):
        super().__init__(-15, 5, -2, 10, None)

class Katana(Weapon):
    def __init__(self):
        super().__init__(-20, 6, -5, 50, None)

class MagicWand(Weapon):
    def __init__(self):
        super().__init__(30, 3, None, None, 3)

class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    def equip_weapon(self, weapon):
        for attr in ATTRS:
            selfattr = getattr(self, attr, None)
            weaponattr = getattr(weapon, attr, None)
            if selfattr is not None and weaponattr is not None:
                setattr(self, attr, max(0, selfattr + weaponattr))

    @property
    def is_alive(self):
        return self.health > 0

    def set_max_health(self):
        self.max_health = getattr(self, 'max_health', self.health)

    def take_hit(self, hit):
        self.set_max_health()
        hitval = max(0, hit - getattr(self, 'defense', 0))
        self.health -= hitval
        return hitval

    def take_heal(self, heal):
        self.set_max_health()
        self.health = min(self.max_health, self.health + heal)

    def heal(self, other):
        pass

    def do_attack(self, other1, other2 = None, **options):
        hit = options.get('hit', self.attack)
        return other1.take_hit(hit)

    def dump(self):
        print('%s: health = %d, attack = %d, defense = %d, vampirism = %f, heal_power = %d' % (
            self.__class__.__name__,
            getattr(self, 'health', 0),
            getattr(self, 'attack', 0),
            getattr(self, 'defense', 0),
            getattr(self, 'vampirism', 0),
            getattr(self, 'heal_power', 0)))

class Healer(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.heal_power = 2
        self.attack = 0

    def heal(self, other):
        other.take_heal(self.heal_power)

class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.attack = 6

    def do_attack(self, other1, other2 = None, **options):
        damage = super().do_attack(other1)
        damage2 = super().do_attack(other2, None, hit = damage / 2) if other2 else 0
        return damage + damage2

class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 50

    def do_attack(self, other1, other2 = None, **options):
        damage = super().do_attack(other1)
        self.take_heal(int(damage * self.vampirism / 100))
        return damage

class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defense = 2

class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7
class Rookie(Warrior):
    def __init__(self):
        super().__init__()
        self.max_health = 50
        self.default_health = 50
        self.attack = 1


class Warlord(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.attack = 4
        self.defense = 2

def fight(unit_1, unit_2):
    while True:
        unit_1.do_attack(unit_2)
        if not unit_2.is_alive:
            return True
        unit_2.do_attack(unit_1)
        if not unit_1.is_alive:
            return False

class Army:
    def __init__(self):
        self.units = []

    def add_unit(self, klass):
        if klass == Warlord and any(isinstance(u, Warlord) for u in self.units):
            return
        self.units.append(klass())

    def add_units(self, klass, count):
        for i in range(count):
            self.add_unit(klass)

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

    def dump(self):
        print(', '.join('%s: %d' % (u.__class__.__name__, u.health) for u in self.units))

class Battle:
    def straight_fight(self, army1, army2):
        while not army1.all_dead() and not army2.all_dead():
            for u1, u2 in zip(army1.units, army2.units):
                fight(u1, u2)
            army1.cleanup()
            army2.cleanup()
        return army2.all_dead()

    def do_turn(self, army1, army2):
        army1.units[0].do_attack(*army2.units[:2])
        if len(army1.units) >= 2:
            army1.units[1].heal(army1.units[0])

    def fight(self, army1, army2):
        army1.move_units()
        army2.move_units()

        army1_turn = True
        while not army1.all_dead() and not army2.all_dead():
            if army1_turn:
                self.do_turn(army1, army2)
            else:
                self.do_turn(army2, army1)
            army1_turn = not army1_turn

            front_warrior_dead1 = army1.cleanup()
            if front_warrior_dead1:
                army1.move_units()

            front_warrior_dead2 = army2.cleanup()
            if front_warrior_dead2:
                army2.move_units()

            if front_warrior_dead1 or front_warrior_dead2:
                # If front warrior died, always restart battle with first army.
                army1_turn = True

        return army2.all_dead()

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