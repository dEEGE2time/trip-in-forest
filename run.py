import os
import time
import sys
import colorama
from colorama import Fore, Back, Style
from pyfiglet import figlet_format


def time_print(string):
    """
    Prints out character by character in a string
    """
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0)


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

    while True:
        intro_choice = input("> " + Fore.YELLOW + "").strip()
        if intro_choice == "1":
            game_launch()
            break
        elif intro_choice == "2":
            print("instructions")
            break
        elif intro_choice == "3":
            print("Exiting game...")
            quit()
        else:
            print(Fore.RED + "Invalid choice, please choose either 1, 2 or 3.")
            print(Fore.YELLOW)


def game_launch():
    """
    Launch game and display story.
    Let player make their first choice.
    """
    cls()
    print(Fore.GREEN + Style.BRIGHT)
    print("Enter your name:")
    name = input("> " + Fore.YELLOW + Style.NORMAL) #make this global
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
    time_print("Except for a light source, which seems to be in the bottom of a very deep hole.\n")
    time_print(". . .\n\n")
    time.sleep(2)
    time_print("You look around and see only pitch black.\n")
    time_print("After your calculations, you can either jump into the hole or stay in this dark space.\n\n")
    time.sleep(1)
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT)
    time_print("Would you like to jump into the hole? (y/n)\n")
    print("+-----------------------------------------------------------------------------+")

    # Provide result based on player choice, stay = death, jump = survive
    while True:
        playerchoice1 = input("> " + Fore.YELLOW + Style.NORMAL).lower().strip()
        if playerchoice1 == "y":
            print(Fore.GREEN + Style.BRIGHT)
            time_print("You jump into the hole...\n")
            hole_choice()
            break
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
            print(Fore.YELLOW)


def hole_choice():
    """
    Player survives and continue game.
    Let player make their second choice.
    """
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

    # Provide result based on player choice, trail = survive, cabin = death
    while True:
        playerchoice2 = input("> " + Fore.YELLOW + Style.NORMAL).lower().strip()
        if playerchoice2 == "trail":
            print(Fore.GREEN + Style.BRIGHT)
            time_print("You follow the trail...\n")
            trail_choice()
            break
        elif playerchoice2 == "cabin":
            print(Fore.GREEN + Style.BRIGHT)
            time_print("You go to the cabin...")
            quit()
        else:
            print(Fore.RED + "Invalid choice, please choose either trail or cabin.\n")
            print(Fore.YELLOW)


def trail_choice():
    """
    Player survives and continue game.
    Let player make their third choice.
    """
    print(Style.NORMAL)
    time_print("You make your way through the trail.\n")
    time_print("It doesn't seem to end...\n")
    time.sleep(1)
    time_print("As you're walking you take notice that everything is moving.\n")
    time_print("The trees, foliage and even the sky, always in motion.\n")
    time_print("You have been walking for hours now.\n")
    time_print(". . .\n\n")
    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT)
    time_print("Hey you! " + Fore.GREEN + Style.NORMAL + "says a rabbit") #change to {name}
    time.sleep(1)
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT)
    time_print("You have to follow me quick!\n")
    time_print("There's no time to explain!")
    print(Fore.GREEN + Style.NORMAL)
    time_print(". . .\n\n")
    time.sleep(2)
    print(Fore.GREEN + Style.BRIGHT)
    time_print("Would you like to follow the rabbit or continue on the trail?\n")
    print("+-----------------------------------------------------------------------------+")

    # Provide result based on player choice, rabbit = survive, trail = death
    while True:
        playerchoice3 = input("> " + Fore.YELLOW + Style.NORMAL).lower().strip()
        if playerchoice3 == "rabbit":
            print(Fore.GREEN + Style.BRIGHT)
            time_print("With quick thinking, you follow the rabbit.\n\n")
            rabbit_choice()
            break
        elif playerchoice3 == "trail":
            print(Fore.GREEN + Style.BRIGHT)
            time_print("With rational thinking, you decide to stay on the trail\n")
            time_print("You keep on walking as the rabbit bounces away.\n")
            time_print(". . .")
            time.sleep(3)
            print(Fore.RED + Style.DIM)
            time_print("\n")
            time.sleep(2)
            time_print("You have been walking for years now, yes, years.\n")
            time.sleep(1)
            time_print("You are but a mindless corpse.\n")
            time.sleep(1)
            time_print("Trapped in the soil of an endless trail.\n")
            time.sleep(1)
            time_print("Walking...\n\n")
            time.sleep(1)
            print(Fore.RED + Style.BRIGHT + "GAME OVER")
            quit()
        else:
            print(Fore.RED + "Invalid choice, please choose either rabbit or trail.\n")
            print(Fore.YELLOW)


def rabbit_choice():
    print(Fore.GREEN + Style.NORMAL)
    time_print("The rabbit is bouncing further in to the woods as you try to follow.\n")
    time_print("You trip on some roots takes a fall.\n") #maybe get character injured for future interactions
    time_print("You look around for the rabbit, but it's gone.\n")
    time_print("You've gone way deep in to be able to find the way back now.")
    time_print(". . .")
    time.sleep(1)
    print(Fore.YELLOW + Style.DIM)
    time_print("Maybe I should've stayed on the trail. " + Fore.GREEN + Style.NORMAL + "You think to yourself.\n\n")
    time_print("You hear a rumbling noise coming from your stomach, you're hungry.\n")
    time_print("You're walking around in the forest as you stumble upon a tasty looking mushroom.\n")
    time.sleep(1)
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT)
    time_print("EAT ME!\n")
    time.sleep(1)
    print(Fore.GREEN + Style.NORMAL)
    time_print("You look around but see nothing.\n")
    time.sleep(1)
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT)
    time_print("BACKSIDE OF THE MUSHROOM GOOF!\n")
    time.sleep(1)
    print(Fore.GREEN + Style.NORMAL)
    time_print("You walk around to see the backside of the mushroom\n")
    time.sleep(1)
    time_print("You're trippin out, screaming and yelling\n")
    print(Fore.YELLOW + Style.BRIGHT)
    time_print("WHAT THE FUCK?!\n")
    time.sleep(1)
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT)
    time_print("HEY, WHAT'S WITH THE RUDE MANNER HERE?\n")
    time.sleep(1)
    print(Fore.YELLOW + Style.BRIGHT)
    time_print("...\n")
    time.sleep(1)
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT)
    time_print("SO YOU GONNA EAT ME OR NO?\n")
    time.sleep(1)
    print(Fore.YELLOW + Style.BRIGHT)
    time_print("...\n\n")
    time.sleep(1)
    print(Fore.GREEN + Style.BRIGHT)
    time_print("Would you like to eat the mushroom? (y/n)\n")
    print("+-----------------------------------------------------------------------------+")


game_intro()