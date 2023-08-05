# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.

label chapterFish:
    scene bg black with fade

    nar "A very very long time ago, we all came from the same origin."

    nar "We all came from the sea."

    show bg water with dissolve

    pause(1)

    show lachlanfish at truecenter with moveinleft:
        zoom 3.0

    pause(1)

    char "It would’ve been nice if we were all like this fish. Not a care in the world; aimlessly swimming the sea. Such a simple creature."

    nar "But you are no simple creature, and so is this fish. This fish is swimming with purpose. And like you, I am very concerned."

    nar "It is concerned for its life; its health; its future. Being worried shows that you care about something, and that something is special to you."

    # Minor choice
    menu:
        "What a sad life it is then. It might as well just not exist if its only purpose is to live.":
            jump fishPurpose
        
        "Maybe I can learn from this fish.":
            jump fishLearn

    # Branch
    label fishPurpose:
        nar "Narrator: Why yes, %(name)s, but no. This fish’s only purpose is not just to live."
    
    label fishLearn:
        nar "Why yes, %(name)s. We all can learn from the simplest things. Now lets see this fish’s true purpose."

    char "What is this fish’s true purpose then?"

    nar "Its purpose is to take a step forward. Find its way out of the water."

    char "Now that’s just stupid. It’s going to die, a very slow… and painful death."

    nar "It is a risk worth taking is it not?"

    menu:
        "No.":
            pause(1)
        "Hmm... I guess so.":
            pause(1)

    nar "Hmm..."

    nar "Would you rather let this fish swim on forever until it dies? Or would you rather take a risk, and take the first step in all of history?"

    # Major choie
    menu:
        "Take the risk":
            jump goodFish
        "Let's stay in a safe place":
            jump badFish

    label goodFish:
        nar "Good"
        jump chapterApe
    
    label badFish:
        scene bg black with fade
        show splashscreen3 with dissolve
    return
