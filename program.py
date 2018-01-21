import random

import time

from actors import Wizard, Creature, SmallAnimal, Dragon

def main():
    print_header()
    # get action inputs from user
    game_loop()

def print_header():
    print('-------------------------------')
    print('     WIZARD BATTLE APP')
    print('-------------------------------')
    print()


def game_loop():
# TODO: randomize the number and types of Creatures to fight
    creature = [
        SmallAnimal('Toad', 1),
        SmallAnimal('Bat', 3),
        Creature('Tiger', 12),
        Dragon('Dragon', 50, 75, True),
        Wizard('Evil Wizard', 1000)
    ]

    hero = Wizard('Ryan', 100)

    while True:
        active_creature = random.choice(creature)
        # TODO: Add proper grammar for print statement below
        print('A {} of level {} has appeared from a dark and foggy forrest'.format(
            active_creature.name, active_creature.level
        ))

        cmd = input('Do you [a]ttack, [r]unaway or [l]ook around?')
        cmd = cmd.lower()
        if cmd == 'a':
            if hero.attack(active_creature):
                creature.remove(active_creature)
            else:
                # TODO: randomize the amount of time that the hero needs to rest based on the level of the opponent
                # he has lost to
                print('The wizard hero runs and hides taking time to recover ...')
                time.sleep(5)
                print('The wizard hero has returned refreshed and invigorated!')
        elif cmd == 'r':
            print('The wizard has become unsure of his power and flees!')
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees:'.format(hero.name))
            for c in creature:
                print('* A {} of level {}'.format(c.name, c.level))
        else:
            print('OK ... exiting game ... good bye!')
            break

        if not creature:
            print('You WIN!')
            break

        print()


if __name__ == '__main__':
    main()