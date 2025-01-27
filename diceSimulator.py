
import random

#1) TAKE THE USER'S INPUT (main function)
#2) PARSE AND VALIDATE DE USER'S INPUT
#3) MAKE THE RANDOM GENERATOR
#4) GENERATE AND DISPLAY THE ASCII DIAGRAM OF DICE FACES


#___________________________________________________2___________________________________________________
def parse_input(input_value):
    """~
    Return `input_value` as an integer between 1 and 6 that the user chose.

    Check if `input_value` is an integer number between 1 and 6.
    If so, return an integer with the same value. Otherwise, tell
    the user to enter a valid number and quit the program.
    """
    if (1 <= input_value <= 6):
        return input_value
    else:
        print("˙⋆✮ Please enter a number from 1 to 6.")
        raise SystemExit(1)

#___________________________________________________3___________________________________________________
#Use random.randint() that will choose one of the numbers between 1 and 6 at a time. 
def roll_dice(num_dice):
    """Return a list of integers with length `num_dice`.

    Each integer in the returned list is a random number between
    1 and 6, inclusive.
    """
    roll_results = []
    #for to create a list of integers between 1 and 6
    #the list will have the same size as the number that the user chose
    for number in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results

#___________________________________________________4___________________________________________________
#Manipulate strings using methods such as .join()
def generate_result(dice_values):
    """Return an ASCII diagram of dice faces from `dice_values`.

    The string returned contains an ASCII representation of each die.
    For example, if `dice_values = [4, 1, 3, 2]` then the string
    returned looks like this:

    """
    # Generate a list of dice faces from DICE_FACES
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_FACES[value])

    # Generate a list containing the dice faces rows
    dice_faces_rows = []
    for row_index in range(DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_index])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)

    # Generate header with the word "RESULTS" centered
    width = len(dice_faces_rows[0])
    diagram_header = "✮ ⭑⋆｡°✩ RESULTS ᯓ★ ⋆⭒˚.⋆"

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram


#Dice faces to display
DICE_FACES = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_FACES[1])
DIE_WIDTH = len(DICE_FACES[1][0])
DIE_FACE_SEPARATOR = " "


#Generate the Diagram of Dice Faces

#Finish Up the App’s Main Code and Roll the Dice

#Refactor the Code That Generates the Diagram of Dice Faces



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ App's main code block ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#1) Take the User's Input
num_dice_input = int(input("How many dice do you want to roll (between 1 and 6)? "))
num_dice = parse_input(num_dice_input)
print("You chose to roll", num_dice , "dices.") #debugging purposes only

#2) Roll the dice
roll_results = roll_dice(num_dice)
print("List of dice faces you got randomly:", roll_results)  #debugging purposes only

#3) Generate the diagram of dice faces
dice_face_diagram = generate_result(roll_results)

#4) Display the diagram
print(f"\n{dice_face_diagram}")
