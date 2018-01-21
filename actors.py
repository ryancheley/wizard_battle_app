import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return 'Creature {} of level {}'.format(self.name, self.level)

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    def attack(self, other_creature):
        print('The wizard {} attacks {}!'.format(
            self.name, other_creature.name
        ))

        # TODO: make more complex algorithm
        my_roll = self.get_defensive_roll()
        creature_roll = other_creature.get_defensive_roll()

        print('You rolled {} ...'.format(my_roll))
        print('The creature {} rolled a {}'.format(other_creature.name, creature_roll))

        if my_roll >= creature_roll:
            print('The wizard has BESTED the creature {}!'.format(other_creature.name))
            return True
        else:
            print('You have been DEFEATED by the creature {}.'.format(other_creature.name))
            return False


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Predator(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll * 4


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breathes_fire):
        super().__init__(
            name,
            level
        )
        self.scaliness = scaliness
        self.breathes_fire = breathes_fire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breathes_fire else 1
        scale_modifier = self.scaliness / 10

        return base_roll * fire_modifier * scale_modifier

