import random
import time
from actors import Wizard, Creature, SmallAnimal, Dragon


def main():
    print_header()
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
        if active_creature.name[0] == 'E':
            print('An {} of level {} has appeared from a dark and foggy forrest'.format(
                active_creature.name, active_creature.level
            ))
        else:
            print('A {} of level {} has appeared from a dark and foggy forrest'.format(
                active_creature.name, active_creature.level
            ))

        cmd = input('Do you [a]ttack, [r]unaway or [l]ook around?')
        cmd = cmd.lower()
        if cmd == 'a':
            if hero.attack(active_creature):
                creature.remove(active_creature)
            else:
                # he has lost to
                wait_time = 15 if active_creature.level >= 15 else active_creature.level
                print('The wizard hero runs and hides taking {} seconds to recover ...'.format(wait_time))
                time.sleep(wait_time)
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