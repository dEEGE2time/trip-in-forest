# Trip in Forest

A python text-based adventure game set in a fantasy world. The players objective is to find a way to the ending, there are in total of two endings as the time of writing this. The user will come across choices resulting in death/survival and also get the change to collect items if the player desires. These items will affect how the game is played out.

View the live website [here](https://trip-in-forest.herokuapp.com/).

![Mockup]()

## Table of Contents
<hr>

1. [Tutorial](#tutorial)
2. [Features](#features)
3. [Technologies](#technologies)
4. [Testing](#testing)
    1. [CI Python Linter](#ci-python-linter)
    2. [Functional Testing](#functional-testing)
5. [Bugs](#bugs)
6. [Deployment](#deployment)
    1. [Deploying through github pages](#deploying-through-github-pages)
    2. [Fork other repositories](#fork-other-repositories)
    3. [Clone other repositories](#clone-other-repositories)
7. [Credits](#credits)
    1. [Content](#content)

## **Tutorial**
<hr>

As a text-based adventure game, all you need is a keyboard. The game will present choices for the player to make and they simply types what it wants to do. The goal is to survive through the story.

When first starting the game the player will be presented with a main menu and the title.
Here the player can choose to
* 1. Start Game
* 2. Instructions
* 3. Exit Game

These three options state the obvious, would the player type "1" into the input field, the game starts and the player get to choose their name. All inputs do not go by numbers, the player will sometimes have to answer with "y" for yes or "n" for no. The game will also asks questions such as "Would you like to walk or run?" and the player will have to enter "walk" or "run". All the choices that player has to make will be displayed for them.

If the player makes a typo or an answer unrelated to the situation, the game will tell them the input is invalid and will ask them to try again, capital letters and spaces do not matter.

When player dies/wins they will be asked to play again if they wish to do so.

## **Features**
<hr>

* Main Menu
    * First page of the game presented with three options.

    1. Start Game
        * Clears the screen
        * Starts game
    2. Instructions
        * Clears the screen
        * Display Instructions
    3. Exit Game
        * Quits the game

![Main Menu](docs/readme-images/features/)
<hr>

* Instructions
    * Displays intructions so the player knows how to play.
    * Press "Q" to clear the screen and return to main menu.

![Instructions](docs/readme-images/features/)
<hr>

* Username
    * Player can choose their own username for the duration of that game.
    * An empty name will result as an invalid input.

![Username](docs/readme-images/features/)
<hr>

* Choices
    * At every point the game asks you a question, you will be presented with two choices.
    * Player makes choice by typing into the input field.
    * Different routes and different endings depending on choice.

![Choices](docs/readme-images/features/) 
<hr>

* Items
    * Player will encounter items they will be asked if they want to pick up.
    * Items can impact gameplay and endings.
    * Some items can not be gathered if they don't meet the requirements for it.

![Items](docs/readme-images/features/)
<hr>

* Announcements
    * Game will display in the terminal whether the player has lost or won.
    * Game will display in the terminal all choices the player makes.

![Announcements](docs/readme-images/features/)
<hr>

* Replay
    * Give the player an option to replay if they lose or win.

![Replay](docs/readme-images/features/)

## **Technologies**
<hr>

* Python
    * Programming language for development of the game.

<br>

* [Github](https://github.com/)
    * Source code hosted on github and deployed through github pages.

<br>

* [Git](https://git-scm.com/)
    * Commit and pushing code using git

<br>

* [Heroku](https://www.heroku.com/home)
    * Deployment of game.

<br>

* Library [black](https://pypi.org/project/black/)
    * Used to format code.

<br>

* Library [colorama](https://pypi.org/project/colorama/)
    * Used to change font color.

<br>

* Library [pyfiglet](https://pypi.org/project/pyfiglet/0.7/)
    * Convert strings to ASCII font art.

<br>

* Module [time](https://docs.python.org/3/library/time.html)
    * Used to make delays between strings.
    * Used with [sys](https://docs.python.org/3/library/sys.html) to print character by character in a string.

<br>

* Module [sys](https://docs.python.org/3/library/sys.html)
    * Used with [time](https://docs.python.org/3/library/time.html) to print character by character in a string.

## **Testing**
<hr>

### **CI Python Linter**

Results:
All clear, no errors found

![ci_python_linter](docs/readme-images/testing/ci_python_linter.png)

### **Functional Testing**
<br>

I manually tested every combination of choices myself, all outputs worked as expected.
<br>

## **Bugs**
<hr>

* When typing during dialogue, correct input will display as invalid.
* Colorama will sometimes display wrong color after invalid input.

Bugs will be fixed in the future as I do not have the time due to project deadline or the knowledge.
<br>

## **Deployment**
<hr>

The website was deployed through the use of GitHub Pages, a feature built in to GitHub.

### **Deploying through github pages**
1. In your repository, click on "Settings" from the top of the menu.
2. In the side menu to your left, click "Pages" in "Code and automation" section.
3. Set "Source" to "Deploy from branch".
4. Set desired branch and set director to /(root).
5. Click "Save" and wait for github to display your URL at the top of this page.
<br>

### **Fork other repositories**
1. Go to desired repository.
2. Click "Fork" in the upper-right corner.
3. Select owner, set repository name and add description(optional).
4. Choose to copy default or all branches.
5. Click "Create Form".
<br>

### **Clone other repositories**
1. In your selected repository, click "Code" drop down button.
2. Select desired cloning method (HTTP)
3. Copy repository to clipboard
4. Open IDE of choice.
5. Type "git clone copied-git-url" into the IDE terminal. (Need git installed) 
<br>

## **Credits**
<hr>

* [Clear interpreter console](https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console)
    * Used this forum as a tutorial for clearing the interpreter console.
    
<br>

* [Print one character by character in a string](https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line)
    * Used this forum as a tutorial for printing character by character in strings.

<br>

* [Colorama - Font color](https://pypi.org/project/colorama/)
    * Different font colors depending on which dialogue. (Blue = NPC, Red = Lose etc..)

<br>

* [Pyfiglet - ASCII font art](https://pypi.org/project/pyfiglet/0.7/)
    * ASCII font art for main menu title.

<br>

* Mentor, Daisy Mc Girr
<br>