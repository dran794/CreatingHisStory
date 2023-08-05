# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define char = Character("You")
define nar = Character("Narrator", color = "#797777")




# The game starts here.

label chapterFish:

     scene bg water

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory
    nar "Hi"

    return
