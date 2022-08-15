import random
import pypokedex


def generate_pokemon():
    pokemon_team = []
    team_size = 5

    for i in range(team_size):
        pokemon_team.append(pypokedex.get(dex=(random.randint(1, 152))))
    return pokemon_team


def pokedex_list(pokemon_team):
    print()
    print(pokemon_team.name)
    print(pokemon_team.base_stats)


def select_main(pokemans):
    poke_names = []
    for i in pokemans:
        print()
        print(i.name)
        poke_names.append(i.name)

    print()
    main_pokemon_name = str(input("Please enter the name number of your main pokemon: "))

    if main_pokemon_name in poke_names:
        main_pokemon = pypokedex.get(name=main_pokemon_name)
        print("\nYour new main pokemon is: " + main_pokemon.name)
        print()
        return main_pokemon.name
    else:
        print("\nThat pokemon is not on the list, choose again:")
        select_main(pokemans)
