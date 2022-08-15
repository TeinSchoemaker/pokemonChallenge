import random
import time

import pypokedex as pypokedex


def initiate_fight(main_pokemon):
    player = pypokedex.get(name=main_pokemon)
    enemy = pypokedex.get(dex=(random.randint(1, 152)))

    print("The fight begins! \n")
    print(f"It's {player.name} VS {enemy.name} \n")
    print("Who will move first?! \n")
    time.sleep(1)

    first_move(player, enemy)


def first_move(player, enemy):
    if player.base_stats.speed >= enemy.base_stats.speed:
        print(f"{player.name} moves first!\n")
        first = player.name
    else:
        print(f"{enemy.name} moves first!\n")
        first = enemy.name
    time.sleep(1)
    fighting(player, enemy, first)


def fighting(player, enemy, first):
    player_hp = player.base_stats.hp
    enemy_hp = enemy.base_stats.hp

    while player_hp > 0 and enemy_hp > 0:
        if first == player.name:
            enemy_hp -= damage(player, enemy)
            print(f"{enemy.name} has " + enemy_hp.__str__() + " health left!!!\n")
            time.sleep(1)
            player_hp -= damage(enemy, player)
            print(f"{player.name} has " + player_hp.__str__() + " health left!!!\n")
            time.sleep(1)
        else:
            player_hp -= damage(enemy, player)
            print(f"{player.name} has " + player_hp.__str__() + " health left!!!\n")
            time.sleep(1)
            enemy_hp -= damage(player, enemy)
            print(f"{enemy.name} has " + enemy_hp.__str__() + " health left!!!\n")
            time.sleep(1)

    if player_hp <= 0:
        print(f"{enemy.name} won!!!")
    elif enemy_hp <= 0:
        print(f"{player.name} won!!!")


def damage(self, other):
    base_damage = 25
    damage_amount = base_damage + (self.base_stats.attack - other.base_stats.defense)
    print(f"{self.name} does " + damage_amount.__str__() + f" points of damage to {other.name}!")
    return damage_amount
