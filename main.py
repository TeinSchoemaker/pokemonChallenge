import fight
import pokedex


def main_menu(pokemon_team):
    global main_pokemon

    print("\nIt's time to D-D-D-D-D-D-D-DUEL!!!")
    print("\nCurrent Main Pokemon: " + main_pokemon)
    print("[1] Fight!")
    print("[2] List all Pokemon")
    print("[3] Select main Pokemon")
    print("[0] Exit")

    option = int(input("Enter your option: "))
    if option == 1:
        if main_pokemon != no_main_pokemon:
            fight.initiate_fight(main_pokemon)
        else:
            print("\n Please select a main pokemon to fight with first! \n")
    elif option == 2:
        player_team = map(pokedex.pokedex_list, pokemon_team)
        print(list(player_team))
        print()
    elif option == 3:
        main_pokemon = pokedex.select_main(pokemon_team)
    elif option == 0:
        exit()
    else:
        print("Invalid option.")
    main_menu(pokemon_team)
    print()


no_main_pokemon = "No main pokemon selected"
main_pokemon = no_main_pokemon
main_menu(pokedex.generate_pokemon())
