import os
import time
import sys
from colorama import Fore, Style
from pyfiglet import figlet_format

# main menu list
mm_options = ["Play Game", "Instructions", "Exit Game"]

# global variables
rope = False
name = ""
mshroom = False
crystal = False


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
    os.system("cls" if os.name == "nt" else "clear")


def game_intro():
    """
    Display intro for player and get player input
    """
    print(
        Fore.GREEN
        + Style.BRIGHT
        + (
            "+--------------------------------------"
            "---------------------------------------+"
        )
    )
    print(figlet_format("Trip in forest", font="larry3d", justify="center"))
    print(
        "+--------------------------------------"
        "---------------------------------------+"
    )
    print(f"1. {mm_options[0]}")
    print(f"2. {mm_options[1]}")
    print(f"3. {mm_options[2]}")
    print(
        "+--------------------------------------"
        "---------------------------------------+"
    )

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


def get_name():
    print(Fore.GREEN + Style.BRIGHT)
    global name
    print("Enter your name:")
    while True:
        name = input("> " + Fore.YELLOW + Style.NORMAL)
        if name == "":
            print(
                Fore.RED + "Invalid name,"
                " please have atleast one character."
            )
            print(Fore.YELLOW)
            continue
        else:
            print(Fore.GREEN + Style.NORMAL)
            time_print(
            f"Hello {Fore.YELLOW+Style.BRIGHT + name + Style.NORMAL+Fore.GREEN}"
            + ", welcome to..."
            )
            break

def game_launch():
    """
    Launch game and display story.
    Let player make their first choice.
    """
    cls()
    get_name()
    time.sleep(2)
    cls()

    print(Fore.GREEN + Style.BRIGHT)
    time_print("TRIP IN FOREST\n\n")
    print(
        "+--------------------------------------"
        "---------------------------------------+"
    )
    time.sleep(3)
    print(Fore.GREEN + Style.NORMAL)
    time_print(
        "You see lights, colors, geometrical shapes "
        "and a bright shimmer in the distance.\n"
    )
    time_print(
        "You feel like you're traveling at unnatural speeds"
        " against the shimmer of lights.\n"
    )
    time_print("Everything gets so bright your eyes start to hurt.\n")
    time_print(". . .\n\n")
    time.sleep(2)
    time_print("You feel yourself getting sucked in...\n")
    time_print("Suddenly everything goes dark.\n")
    time_print(
        "Except for a light source, which seems"
        " to be in the bottom of a very deep hole.\n"
    )
    time_print(". . .\n\n")
    time.sleep(2)
    time_print("You look around and see only pitch black.\n")
    time_print(
        "After your calculations, you can either jump"
        " into the hole or stay in this dark space.\n"
    )
    time_print(". . .\n\n")
    time.sleep(2)
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT)
    time_print("Would you like to jump into the hole? (y/n)\n")
    print(
        "+--------------------------------------"
        "---------------------------------------+"
    )

    # Provide result based on player choice, stay = death, jump = survive
    while True:
        choice_hole = input("> " + Fore.YELLOW + Style.NORMAL).lower().strip()
        if choice_hole == "y":
            print(Fore.GREEN + Style.BRIGHT)
            time_print("You jump into the hole...\n")
            time.sleep(2)
            hole_area()
            break
        elif choice_hole == "n":
            print(Fore.GREEN + Style.BRIGHT)
            time_print("You decide to stay...\n")
            time.sleep(3)
            print(Fore.RED + Style.DIM)
            time_print("You stayed in this dark space for weeks...\n")
            time.sleep(1)
            time_print(
                "You eventually went insane"
                " and starved to death...\n\n"
                )
            time.sleep(1)
            print(Fore.RED + Style.BRIGHT + "GAME OVER")
            quit()
        else:
            print(Fore.RED + "Invalid choice, please choose either y or n.\n")
            print(Fore.YELLOW)


def hole_area():
    """
    Player survives hole and continues game.
    Let player make their second choice.
    """
    print(Style.NORMAL)
    time_print("You're falling towards the distant light.\n")
    time_print("The fall is long and it takes a while.\n")
    time_print(
        "When you break through,"
        " you're levitating just above ground.\n"
        )
    time_print(". . .\n\n")
    time.sleep(2)
    time_print(
        "You find yourself in a forest,"
        " unfamiliar yet familiar to you.\n"
        )
    time_print("Plants and flowers as huge as trees.\n")
    time_print("And trees as huge as... Well you get the idea.\n")
    time_print(". . .\n\n")
    time.sleep(2)
    time_print("You see a trail leading into the woods.\n")
    time_print("And a lonely cabin in the opposite direction.\n")
    time_print(". . .\n\n")
    time.sleep(2)
    print(Style.BRIGHT)
    time_print("Would you like to follow the trail or go to the cabin?\n")
    print(
        "+--------------------------------------"
        "---------------------------------------+"
    )

    # Provide result based on player choice, trail = path 1, cabin = path 2
    while True:
        choice_trail_cabin = input(
            "> " + Fore.YELLOW + Style.NORMAL
            ).lower().strip()
        if choice_trail_cabin == "trail":
            print(Fore.GREEN + Style.BRIGHT)
            time_print("You follow the trail...\n")
            time.sleep(2)
            trail_area()
            break
        elif choice_trail_cabin == "cabin":
            print(Fore.GREEN + Style.BRIGHT)
            time_print("You go to the cabin...\n")
            time.sleep(2)
            cabin_area()
            break
        else:
            print(
                Fore.RED + "Invalid choice,"
                " please choose either trail or cabin.\n"
            )
            print(Fore.YELLOW)


def trail_area():
    """
    Player chose trail and continues game.
    Let player make their third choice (path 1).
    """
    print(Style.NORMAL)
    time_print("You make your way through the trail.\n")
    time_print("It doesn't seem to end...\n")
    time_print(
        "As you're walking you take notice"
        " that everything is moving.\n"
        )
    time_print("The trees, foliage and even the sky, always in motion.\n")
    time_print("You have been walking for hours now.\n")
    time_print(". . .\n\n")
    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT)
    time_print(
        f"Hey {name}! "
        + Fore.GREEN + Style.NORMAL + "says a rabbit"
    )
    time.sleep(1)
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT)
    time_print("You have to follow me quick!\n")
    time_print("There's no time to explain!")
    print(Fore.GREEN + Style.NORMAL)
    time_print(". . .\n\n")
    time.sleep(2)
    print(Fore.GREEN + Style.BRIGHT)
    time_print(
        "Would you like to follow the rabbit"
        " or continue on the trail?\n"
        )
    print(
        "+--------------------------------------"
        "---------------------------------------+"
    )

    # Provide result based on player choice, rabbit = survive, trail = death
    while True:
        choice_rabbit_trail = input(
            "> " + Fore.YELLOW + Style.NORMAL
            ).lower().strip()
        if choice_rabbit_trail == "rabbit":
            print(Fore.GREEN + Style.BRIGHT)
            time_print("With quick thinking, you follow the rabbit...\n\n")
            time.sleep(2)
            rabbit_area()
            break
        elif choice_rabbit_trail == "trail":
            print(Fore.GREEN + Style.BRIGHT)
            time_print(
                "With rational thinking,"
                " you decide to stay on the trail\n"
                )
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
            print(
                Fore.RED + "Invalid choice,"
                " please choose either rabbit or trail.\n"
            )
            print(Fore.YELLOW)


def cabin_area():
    """
    Player chose cabin and continues game.
    Let player make their third choice (path 2).
    """
    print(Fore.GREEN + Style.NORMAL)
    time_print("The door was open so you enter the cabin.\n")
    time_print("It seems familiar to you.\n")
    time_print("You explore around and see a staircase down to a cellar.\n")
    time_print(". . .\n\n")
    print(Style.BRIGHT)
    time_print("Would you like to explore the cellar? (y/n)\n")
    print(
        "+--------------------------------------"
        "---------------------------------------+"
    )

    while True:
        choice_cellar = input("> " + Fore.YELLOW).lower().strip()
        if choice_cellar == "y":
            print(Fore.GREEN)
            time_print("You decide to explore the cellar...\n")
            time.sleep(2)
            cellar_area()
            break
        elif choice_cellar == "n":
            print(Fore.GREEN)
            time_print("You leave the house and follow the trail instead...\n")
            time.sleep(2)
            trail_area()
            break
        else:
            print(Fore.RED + "Invalid choice, please choose either y or n.\n")
            print(Fore.YELLOW)


def cellar_area():
    """
    Continue game after cabin area.
    Give player option to collect item.
    Item will have use in future interactions.
    """
    print(Style.NORMAL)
    time_print(
        "In the cellar you see a rope holding together"
        " two beams that is supporting the cabin.\n"
    )
    time_print(
        "You could collect the rope"
        " but the cabin is old and unsteady.\n"
        )
    time_print(". . .\n")
    time.sleep(2)
    print(Fore.YELLOW + Style.DIM)
    time_print(
        "I could collect the ropes but it's risky, the cabin might collapse. "
        + Fore.GREEN
        + Style.NORMAL
        + "You think to yourself.\n"
    )
    time_print(". . .\n\n")
    time.sleep(2)
    print(Style.BRIGHT)
    time_print("Would you like to collect the rope? (y/n)\n")
    print(
        "+--------------------------------------"
        "---------------------------------------+"
    )
    global rope
    while True:
        choice_rope = input("> " + Fore.YELLOW).lower().strip()
        if choice_rope == "y":
            print(Fore.GREEN)
            time_print("You collected the rope...\n")
            time_print(
                "You took a chance and"
                " the building seems to be fine.\n"
                )
            rope = True
            time.sleep(2)
            after_rope_area()
            break
        elif choice_rope == "n":
            print(Fore.GREEN)
            time_print("You decide not to collect the rope...\n")
            time.sleep(2)
            after_rope_area()
            break
        else:
            print(Fore.RED + "Invalid choice, please choose either y or n.\n")
            print(Fore.YELLOW)


def after_rope_area():
    """
    Continue game after cellar area.
    Check if player collected item.
    Different outcome depending on item is
    collected or not.
    """
    print(Style.NORMAL)
    time_print(
        "Looking around in the cellar"
        " you notice a hole behind a shelf.\n"
        )
    time_print("You move the shelf and find a underground path.\n")
    time_print("With curiosity you decide to explore this path.\n")
    time_print(". . .\n\n")
    time.sleep(2)
    time_print("As you enter, the entrance behind you seals.\n")
    time_print(
        "The path is very dark,"
        " but soon you find yourself in a cave.\n"
        )
    cave_area()


def cave_area():
    """
    Continue game after cellar or grass patch areas.
    Check if player has necessary items to do interactions.
    Different outcomes depending on if
    player has collected items or not.
    """
    time_print("Torches has been lit up here so you are able to see.\n")
    time_print("You look around and see a shiny crystal in the ceiling.\n")
    time_print(". . .\n")
    time.sleep(2)
    print(Style.BRIGHT)
    time_print("Would you like to grab the crystal? (y/n)\n")
    print(
        "+--------------------------------------"
        "---------------------------------------+"
    )

    global mshroom
    global crystal
    global rope
    choice_crystal = input("> " + Fore.YELLOW).lower().strip()
    while True:
        if rope is True:
            if choice_crystal == "y":
                print(Fore.GREEN)
                time_print(
                    "You use your rope to climb"
                    " up and grab the crystal.\n"
                    )
                crystal = True
                time.sleep(2)
                cave_exit()
                break
            elif choice_crystal == "n":
                print(Fore.GREEN)
                time_print("You decide to not grab the crystal.\n")
                time.sleep(2)
                cave_exit()
                break
            else:
                print(
                    Fore.RED + "Invalid choice,"
                    " please choose either y or n.\n"
                    )
                print(Fore.YELLOW)
        if mshroom is True:
            if choice_crystal == "y":
                print(Fore.GREEN)
                time_print("You're not sure how to reach the crystal.\n")
                print(Fore.YELLOW)
                time_print(
                    "Don't worry I got it, just reach out your hands. "
                    + Fore.GREEN
                    + "Says the mushroom.\n"
                )
                time_print(
                    "The mushroom seemed to use its mind"
                    " to teleport the crystal into your hands.\n"
                )
                crystal = True
                time.sleep(2)
                cave_exit()
                break
            elif choice_crystal == "n":
                print(Fore.GREEN)
                time_print("You decide to not grab the crystal.\n")
                time.sleep(2)
                cave_exit()
                break
            else:
                print(
                    Fore.RED + "Invalid choice,"
                    " please choose either y or n.\n"
                )
                print(Fore.YELLOW)
        if rope is False:
            if choice_crystal == "y":
                print(Fore.GREEN)
                time_print(
                    "You do not have anything"
                    " to grab the crystal with.\n"
                    )
                print(Fore.YELLOW + Style.DIM)
                time_print(
                    "Maybe the rope would've come in handy... "
                    + Fore.GREEN
                    + Style.BRIGHT
                    + "You think to yourself.\n"
                )
                time.sleep(2)
                cave_exit()
                break
            elif choice_crystal == "n":
                print(Fore.GREEN)
                time_print("You decide to not grab the crystal.\n")
                time.sleep(2)
                cave_exit()
                break
            else:
                print(
                    Fore.RED + "Invalid choice,"
                    " please choose either y or n.\n"
                )
                print(Fore.YELLOW)


def cave_exit():
    """
    Continue game after cave area.
    Player is able to win if items
    are in possession.
    Lose if not.
    """
    print(Style.NORMAL)
    time_print("You continue walking through the cave.\n")
    time_print("You finally see an exit.\n")
    time_print("You're walking towards that exit.\n")
    time_print(". . .\n\n")
    time.sleep(2)
    time_print("As you exit the cave, you find yourself in a white space.\n")
    time_print(
        "In front of you, there's a stone structure,"
        " as tall as a door.\n"
        )
    time_print("You look around and the cave behind you is gone.\n")
    time_print(". . .\n\n")
    time.sleep(2)
    time_print(
        "You inspect this stone structure"
        " and find a keyhole, shaped like a crystal.\n"
    )
    time.sleep(2)
    if crystal is True:
        print(Style.BRIGHT)
        time_print(
            "You reach for the crystal you"
            " collected and place it in the keyhole.\n"
        )
        time_print(". . .\n\n")
        time.sleep(2)
        time_print("You feel a tremble on the surface you're standing on.\n")
        time.sleep(2)
        time_print("You suddenly get sucked into the crystal.\n\n")
        time.sleep(2)
        player_win()
    if crystal is False:
        time_print("You reach for your pockets.\n")
        time.sleep(2)
        time_print("You do not seem to have any that fits the keyhole.\n")
        if mshroom is True:
            time.sleep(2)
            print(Fore.YELLOW + Style.BRIGHT)
            time_print(
                "You're f#cked. "
                + Fore.GREEN + Style.NORMAL + "Says the mushroom.\n"
            )
        time_print(". . .\n\n")
        time.sleep(2)
        print(Fore.RED + Style.BRIGHT)
        time_print("You are stuck here...\n")
        time.sleep(2)
        time_print("Eternally.\n\n")
        time.sleep(2)
        print("GAME OVER")
        # play_again()


def player_win():
    """
    Display ending for player.
    Player has won.
    """
    print(Fore.GREEN + Style.NORMAL)
    global name
    time_print("You're back where you're once was.\n")
    time_print(
        "Floating in a space with lights,"
        " colors and geometrical shapes.\n"
    )
    time_print("Traveling at unnatural speeds.\n")
    time_print(". . .\n\n")
    time.sleep(2)
    time_print("Suddenly, everything goes dark.\n")
    time_print("You open your eyes and find yourself in your apartment.\n")
    time_print("You're laying on the floor.\n")
    time_print(". . .\n\n")
    print(Fore.LIGHTBLUE_EX)
    time_print(f"Hey {name}, are you alright?!\n")
    time_print("We thought we lost you.\n\n")
    print(Fore.GREEN)
    print("YOU WIN")
    # play_again()


def rabbit_area():
    """
    Player survives trail and continues game.
    Let player make their fourth choice (path 1)
    """
    print(Fore.GREEN + Style.NORMAL)
    time_print(
        "The rabbit is bouncing further"
        " in to the woods as you try to follow.\n"
    )
    time_print("You trip on some roots and take a fall.\n")
    time_print(". . .\n\n")
    time.sleep(2)
    time_print("You look around for the rabbit, but it's gone.\n")
    time_print(
        "You've gone way deep in to be"
        " able to find the way back now.\n"
    )
    time_print(". . .\n\n")
    time.sleep(2)
    print(Fore.YELLOW + Style.DIM)
    time_print(
        "Maybe I should've stayed on the trail. "
        + Fore.GREEN
        + Style.NORMAL
        + "You think to yourself.\n\n"
    )
    time_print(
        "You hear a rumbling noise"
        " coming from your stomach, you're hungry.\n"
    )
    time_print(
        "You're walking around in the forest as"
        " you stumble upon a tasty looking mushroom.\n"
    )
    time_print(". . .\n")
    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT)
    time_print("EAT ME!\n")
    time.sleep(1)
    print(Fore.GREEN + Style.NORMAL)
    time_print("You look around but see nothing...\n")
    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT)
    time_print("BACKSIDE OF THE MUSHROOM GOOF!\n")
    time.sleep(1)
    print(Fore.GREEN + Style.NORMAL)
    time_print("You walk around to see the backside of the mushroom.\n")
    time.sleep(1)
    time_print("You're trippin out, screaming and yelling\n")
    print(Fore.YELLOW + Style.BRIGHT)
    time_print("WHAT THE F#CK?!\n")
    time.sleep(1)
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT)
    time_print("HEY, WHAT'S WITH THE RUDE MANNER HERE?\n")
    time.sleep(1)
    print(Fore.YELLOW + Style.BRIGHT)
    time_print("...\n")
    time.sleep(1)
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT)
    time_print("SO YOU GONNA EAT ME OR NOT?\n")
    time.sleep(1)
    print(Fore.YELLOW + Style.BRIGHT)
    time_print("...\n\n")
    time.sleep(1)
    print(Fore.GREEN + Style.BRIGHT)
    time_print("Would you like to eat the mushroom? (y/n)\n")
    print(
        "+--------------------------------------"
        "---------------------------------------+"
    )

    while True:
        choice_mshroom = input("> " + Fore.YELLOW).lower().strip()
        if choice_mshroom == "y":
            print(Fore.GREEN)
            time_print("You eat the mushroom...\n\n")
            time.sleep(3)
            print(Fore.RED + Style.BRIGHT)
            time_print("You die of food poisoning.\n")
            time_print("Tragic...\n\n")
            print("GAME OVER")
            quit()
        elif choice_mshroom == "n":
            print(Fore.GREEN)
            time_print("You choose not to eat the mushroom...\n\n")
            time.sleep(2)
            mshroom_area()
            break
        else:
            print(Fore.RED + "Invalid choice, please choose either y or n.\n")
            print(Fore.YELLOW)


def mshroom_area():
    """
    Continue game after rabbit area.
    Gives player choice to collect mushroom.
    Different outcomes will occur if
    mushroom has been collected or not.
    """
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT)
    time_print("Bummer...\n")
    time.sleep(1)
    time_print("You see, I've been stuck here since the beginning of time.\n")
    time_print("Hell, probably before that too.\n\n")
    time.sleep(1)
    time_print("How about you take me with you eh?\n")
    time_print("I could be your companion, whaddya say?\n")
    time_print(". . .\n")
    time.sleep(1)
    print(Fore.GREEN)
    time_print("Would you like to bring the mushroom with you? (y/n)\n")
    print(
        "+--------------------------------------"
        "---------------------------------------+"
    )

    while True:
        global mshroom
        choice_mshroom_bring = input("> " + Fore.YELLOW).lower().strip()
        if choice_mshroom_bring == "y":
            print(Fore.GREEN)
            print("You bring mushroom...\n")
            time.sleep(2)
            mshroom = True
            after_mshroom_area()
            break
        elif choice_mshroom_bring == "n":
            print(Fore.GREEN)
            print("You don't bring mushroom...\n")
            time.sleep(2)
            after_mshroom_area()
            break
        else:
            print(Fore.RED + "Invalid choice, please choose either y or n.\n")
            print(Fore.YELLOW)


def after_mshroom_area():
    """
    Player continues game.
    Outcome depending on whether the player
    picked up the mushroom or not.
    """
    global mshroom
    if mshroom is True:
        print(Fore.LIGHTBLUE_EX)
        time_print("Let me tell you a secret.\n")
        time_print(". . .\n\n")
        time.sleep(2)
        time_print("You see that empty patch of grass over there?\n")
        time_print("There's a secret passage below it.\n")
        print(Fore.GREEN + Style.NORMAL)
        time_print(". . .\n")
        print(Style.BRIGHT)
        time_print("Would you like to explore the patch of grass? (y/n)\n")
        print(
            "+--------------------------------------"
            "---------------------------------------+"
        )

        while True:
            choice_grasspatch = input("> " + Fore.YELLOW).lower().strip()
            if choice_grasspatch == "y":
                print(Fore.GREEN)
                time_print("You explore the patch of grass...\n")
                time.sleep(2)
                grasspatch_area()
                break
            elif choice_grasspatch == "n":
                print(Fore.GREEN)
                time_print("You decide to not explore the patch of grass...\n")
                time.sleep(1)
                print(Fore.LIGHTBLUE_EX)
                time_print(
                    "Man just leave me here then. "
                    + Fore.GREEN
                    + "Says the mushroom.\n"
                )
                time.sleep(1)
                print(Fore.YELLOW)
                time_print("You leave the mushroom.\n")
                time.sleep(1)
                waterfall_area()
                break
            else:
                print(
                    Fore.RED + "Invalid choice,"
                    " please choose either y or n.\n"
                    )
                print(Fore.YELLOW)
    elif mshroom is False:
        waterfall_area()


def waterfall_area():
    """
    Continue game if mushroom not collected
    or if player decides to not explore grass patch.
    Give player option to explore waterfall.
    """
    print(Fore.GREEN + Style.NORMAL)
    time_print("You continue walking the woods.\n")
    time_print("After walking for a while you come across a waterfall.\n")
    time.sleep(1)
    print(Fore.YELLOW + Style.DIM)
    time_print(
        "Maybe there's a secret passage behind that waterfall. "
        + Fore.GREEN
        + Style.NORMAL
        + "You think to yourself.\n"
    )
    time_print(". . .\n")
    time.sleep(2)
    print(Style.BRIGHT)
    time_print("Would you like to explore the waterfall? (y/n)\n")
    print(
        "+--------------------------------------"
        "---------------------------------------+"
    )
    while True:
        choice_waterfall = input("> " + Fore.YELLOW).lower().strip()
        if choice_waterfall == "y":
            print(Fore.GREEN)
            time_print("You decide to explore the waterfall...\n")
            time.sleep(3)
            print(Fore.RED)
            time_print(
                "As you try to enter the waterfall you get slammed"
                " by the body of water falling down on you.\n"
            )
            time_print(
                "You hit your head on some sharp"
                " rocks and starts bleeding out...\n\n"
            )
            print("GAME OVER")
            quit()
        elif choice_waterfall == "n":
            print(Fore.GREEN)
            print("You decide to not explore the waterfall...\n")
            time.sleep(2)
            survive_waterfall()
            break
        else:
            print(
                Fore.RED + "Invalid choice,"
                " please choose either y or n.\n"
                )
            print(Fore.YELLOW)


def survive_waterfall():
    """
    Continue game after waterfall area.
    Second ending for player.
    If player completes riddle, player win.
    Otherwise, player lose.
    """
    global name
    print(Style.NORMAL)
    time_print("You see the same rabbit that you met earlier.\n")
    time_print("You decide to follow the rabbit once again.\n")
    time_print(". . .\n\n")
    time.sleep(2)
    time_print("The rabbit stopped.\n")
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT)
    time_print("Hey! I know you're following me.\n")
    print(Fore.GREEN + Style.NORMAL)
    time_print("You walk up towards the rabbit.\n")
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT)
    time_print(f"Imma be honest with you {name}.\n\n")
    time.sleep(1)
    time_print("Where do you think you're going?\n")
    time_print("Where do you even think you are?\n\n")
    time.sleep(1)
    time_print("No matter, you're near the end.\n")
    time_print("Follow me up this mountain, you don't really have a choice.\n")
    print(Fore.GREEN + Style.NORMAL)
    time_print(". . .\n\n")
    time.sleep(2)
    time_print(
        "As you reach the top of the mountain"
        " you look out on the land.\n"
        )
    time_print(
        "It's finite, like and island but no water,"
        " just an empty void.\n\n"
        )
    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT)
    time_print(f"I have one question for you {name},\n\n")
    time_print("What gets shorter as it gets longer?\n\n")
    time_print("You only get 1 chance.\n")
    print(Fore.GREEN + Style.NORMAL)
    time_print("The rabbit vanishes into thin air.\n\n")
    print(Style.BRIGHT)
    time_print("What gets shorter as it gets longer?\n")
    print(
        "+--------------------------------------"
        "---------------------------------------+"
    )

    riddle_answer = input("> " + Fore.YELLOW).lower().strip()
    if riddle_answer == "life":
        player_win()
    else:
        time_print("Your answer gave no sign of it being correct.\n")
        time.sleep(2)
        print(Fore.RED)
        time_print("The weather up here gets really cold.\n")
        time.sleep(1)
        time_print(
            "It happens fast and suddenly it's"
            " colder than you ever could imagine.\n"
        )
        time.sleep(1)
        time_print("You whole body freezes to ice.\n\n")
        time.sleep(2)
        print("GAME OVER")


def grasspatch_area():
    """
    Continue game after choosing to explore grass patch.
    Second path for first ending.
    Go to cave area.
    """
    print(Style.NORMAL)
    time_print("You're standing on the patch of grass.\n")
    time_print(". . .\n\n")
    time.sleep(2)
    time_print("The ground crumbles as you fall into the ground.\n")
    time_print("You feel a bit dizzy after the fall but you are ok.\n")
    time_print(". . .\n\n")
    time.sleep(2)
    time_print("You look around and find yourself in a cave.\n")
    cave_area()


if __name__ == "__main__":
    game_intro()
