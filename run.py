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
        time.sleep(.05)

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
        print(Fore.RED + "Invalid choice, please choose either 1, 2 or 3.")

def game_launch():
    """
    Launch game and display story
    Let player make their first choice
    """
    cls()
    print(Fore.GREEN + Style.BRIGHT)
    print("Enter your name:")
    name = input("> " + Fore.YELLOW + Style.NORMAL)
    print(Fore.GREEN + Style.NORMAL)
    time_print(f"Hello {Fore.YELLOW + Style.BRIGHT + name + Style.NORMAL + Fore.GREEN}, welcome to...")
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
    time_print("You feel like you're traveling at unnatural speeds against the shimmer of lights.\n")
    time.sleep(.5)
    time_print("Everything gets so bright your eyes start to hurt.\n")
    time_print(". . .\n\n")
    time.sleep(2)
    time_print("You feel yourself getting sucked in...\n")
    time.sleep(.5)
    time_print("Suddenly everything goes dark.\n")
    time.sleep(1)
    time_print("Except for one light which seems to be in the bottom of a very deep hole.\n")
    time_print(". . .\n\n")
    time.sleep(2)
    time_print("You look around and see only pitch black.\n")
    time_print("After your calculations, you can either jump into the hole or stay in this dark space.\n\n")
    time.sleep(1)
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT)
    time_print("Would you like to jump into the hole? (y/n)\n")
    print("+-----------------------------------------------------------------------------+")

    playerchoice1 = input("> " + Fore.YELLOW + Style.NORMAL).lower().strip()
    if playerchoice1 == "y":
        print(Fore.GREEN + Style.BRIGHT)
        time_print("You jump into the hole...\n")
        hole_choice()
    elif playerchoice1 == "n":
        print(Fore.GREEN + Style.BRIGHT)
        time_print("You decide to stay...")
        time.sleep(3)
        print(Fore.RED + Style.DIM)
        time_print("You stayed in this dark space for weeks...\n")
        time.sleep(2)
        time_print("You eventually went insane and starved to death...\n")
        print(Fore.RED + Style.BRIGHT + "GAME OVER")
        quit()
    else:
        print(Fore.RED + "Invalid choice, please choose either y or n.\n")

def hole_choice():
    print(Style.NORMAL)
    time_print("You're falling towards the distant light.\n")
    time_print("The fall is long and it takes a while.\n")
    time_print("When you break through, you're levitating just above ground\n")
    time_print(". . .\n\n")
    time.sleep(2)
    time_print("You find yourself in a forest, unfamiliar yet familiar to you.\n")
    time_print("Plants and flowers as huge as trees.\n")
    time_print("And trees as huge as... Well you get the idea.\n")
    time_print(". . .\n\n")
    time.sleep(2)
    time_print("You see a trail leading into the woods.\n")
    time_print("And a lonely cabin in the opposite direction\n")
    time_print(". . .\n\n")
    time.sleep(2)
    print(Style.BRIGHT)
    time_print("Would you like to follow the trail or go to the cabin?\n")
    print("+-----------------------------------------------------------------------------+")

    playerchoice2 = input("> " + Fore.YELLOW + Style.NORMAL).lower().strip()
    if playerchoice2 == "trail":
        print(Fore.GREEN + Style.BRIGHT)
        time_print("You follow the trail...")
        trail_choice()
    elif playerchoice2 == "cabin":
        print(Fore.GREEN + Style.BRIGHT)
        time_print("You go to the cabin...")
        cabin_choice()
    else:
        print(Fore.RED + "Invalid choice, please choose either trail or cabin.\n")


def trail_choice():
    print("trail choice")

def cabin_choice():
    print("cabin choice")

game_intro()