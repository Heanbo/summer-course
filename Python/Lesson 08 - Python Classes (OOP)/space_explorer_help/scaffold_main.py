import os
from scaffold_spacecraft import Spacecraft
from scaffold_planet import Planet
from scaffold_player import Player
import random


# this just clears the screen
def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    print("=== Welcome to the Space Explorer Game ===")
    player_name = input("Enter your name, Captain: ")

    # choose difficulty

    # initialize variables

    # main game loop
    # while we still have stuff to do...
    # while...
    while True: # replace this condition
        # show the player the current status of the game
        clear_screen()

        # have the player take a game action
        print("\nWhat would you like to do?")
        print("1. Travel to a planet")
        print("2. Buy fuel")
        print("3. Start mission on current planet")
        print("4. End mission.")
        action = input("Enter the number of your choice: ")

        # handle the player's action accordingly
        if action == "1":
            pass
        elif action == "2":
            pass
        elif action == "3":
            pass
        elif action == "4":
            pass
        else:
            print("Invalid action. Please choose 1, 2, 3, or 4.")
            input("Press Enter to continue...")

    clear_screen()

    # show any game stats when the game ends
    pass


if __name__ == "__main__":
    main()
