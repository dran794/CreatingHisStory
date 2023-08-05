﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Lachlan")
define n = Character("Narrator", color = "#797777")



# The game starts here.

label start:
    jump chapterApe

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg water

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show lachlan happy

    # These display lines of dialogue.

    l "Hmmm..."

    l "I wonder what's on the other side..."


    # This ends the game.

    return