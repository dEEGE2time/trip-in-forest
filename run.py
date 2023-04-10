import os
import time
import sys
import colorama
from colorama import Fore, Back, Style
from pyfiglet import figlet_format

def time_print(s):
    """
    Prints out character by character in a string
    """
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.1)

def cls():
    """
    Clears the screen
    """
    os.system('cls'  if os.name=='nt' else 'clear')


def game_intro():
    """
    Display intro for player and get player input
    """
    print(Fore.GREEN + Style.BRIGHT + (
        "+-----------------------------------------------------------------------------+"
        ))
    print(figlet_format("Trip in forest", font="larry3d", justify="center"))
    print("+-----------------------------------------------------------------------------+")
    print("1. Play Game")
    print("2. Instructions")
    print("3. Exit Game")
    print("+-----------------------------------------------------------------------------+")
    intro_choice = input("> " + Fore.YELLOW + "").strip()

    if intro_choice == "1":
        game_launch()
    elif intro_choice == "2":
        print("instructions")
    elif intro_choice == "3":
        print("Exiting game...")
        quit()
    else:
        print(Fore.RED + "Invalid choice, please choose either 1, 2 or 3")

def game_launch():
    """
    Launch game and display story
    """
    cls()
    print(Fore.GREEN + Style.BRIGHT)
    print("Enter your name:")
    name = input("> " + Fore.YELLOW + Style.NORMAL)
    print(Fore.GREEN + Style.NORMAL)
    time_print(f"Hello {name}, welcome to...")
    time.sleep(2)
    cls()

    print(Fore.GREEN + Style.BRIGHT)
    time_print("TRIP IN FOREST\n\n")
    print("+-----------------------------------------------------------------------------+")
    time.sleep(3)
    print(Fore.GREEN + Style.NORMAL)
    time_print("You see lights, colors, geometrical shapes "
            "and a bright shimmer in the distance.\n"
            )
    time.sleep(.5)
    time_print("You feel like you're traveling, with unnatural speed, against the shimmer of lights.\n")
    time.sleep(.5)
    time_print("Everything gets so bright your eyes start to hurt.\n")
    time_print(". . .\n\n")
    time.sleep(2)
    time_print("You find yourself in a forest, unfamiliar yet familiar to you.\n")
    time.sleep(.5)
    time_print("Everything is what it seems to be but also not, at the same time.\n")
    time_print(". . .\n\n")
    time_print("")
    print("+-----------------------------------------------------------------------------+")


game_intro()