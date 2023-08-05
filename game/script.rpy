﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Lachlan")
define n = Character("Narrator", color = "#797777")




# The game starts here.

label start:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg water

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show lachlanfish:
        xalign 0.5
        yoffset 200
        zoom 3.0
        rotate -45.0

    # These display lines of dialogue.

    l "Hmmm..."

    l "I wonder what's on the other side..."

    menu:
        n "Should Lachlan jump to the other side?"
        "Yeah":
            jump fishToApe
        "Nah":
            jump depressedFish

    label depressedFish:
        l "I wanna stay in my comfort zone."
        l "I guess I'll never know what's outside"

        return

    label fishToApe:
        scene bg abovewater
        n "In life..."
        n "you have to take risks sometimes."
        #jump chapterApe

    scene bg sunnyfield:
        zoom 2

    show issaclachy:
        xalign 0.1
        yoffset 300
        zoom 2

    l "Ah, its hot outside..."
    l "I should find some shade."

    #menu:
        #n "Where should I go?"
        #"Under the apple tree":
            #jump
        #"Go back home":
            #jump
        
    label underAppleTree:
        scene bg appletree
        l "Ah... this is nice"
        l "GAH DAMN"
        l "Why did this apple fall down?"
        #jump

    label newtonHome:
        l "Im tired..."
        l "I'm going to go to bed now."


    # This ends the game.

    return
