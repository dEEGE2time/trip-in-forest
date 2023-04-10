import colorama
from colorama import Fore, Back, Style
from pyfiglet import figlet_format

def game_intro():
    """
    Display intro for player and get player input
    """
    print(Fore.GREEN + Style.BRIGHT + ("+-----------------------------------------------------------------------------+"))
    print(figlet_format("Trip in forest", font="larry3d", justify="center"))
    print(("+-----------------------------------------------------------------------------+"))
    print("1. Play Game")
    print("2. Instructions")
    print("3. Exit Game")
    print(("+-----------------------------------------------------------------------------+"))
    intro_choice = input("> " + Fore.YELLOW + "").strip()

    if intro_choice == "1":
        print("play game")
    elif intro_choice == "2":
        print("instructions")
    elif intro_choice == "3":
        print("Exiting game...")
        quit()
    else:
        print(Fore.RED + "Invalid choice, please choose either 1, 2 or 3")

game_intro()