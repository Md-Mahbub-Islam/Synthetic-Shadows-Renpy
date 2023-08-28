# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define alex = Character("Alex", color="#ae10a9")
define olivia = Character("Olivia", color="#02a474")


# images
image bg_diner = "bg/diner.png"
image city_1 = "bg/city_1.png"
image city_2 = "bg/city_2.png"
image city_3 = "bg/city_3.png"



image alex = "ch/alex.png"
image olivia = "ch/olivia.png"

init python:
    # Define attributes and set initial values
    money = 0
    trust = 0
    morality = 50

    health = 100
    attack = 10
    defense = 10


label screen_shake:
    # Play a sound effect if desired.
    # play sound "shake_sound_effect"

    # Number of times to shake the screen.
    $ shake_count = 5

    # Magnitude of the shake (adjust as needed).
    $ shake_magnitude = 8

    # Loop to shake the screen.
    while shake_count > 0:
        $ shake_x = renpy.random.randint(-shake_magnitude, shake_magnitude)
        $ shake_y = renpy.random.randint(-shake_magnitude, shake_magnitude)
        $ shake_count -= 1
        pause 0.03  # Adjust the pause duration for the desired shake speed.

    # Reset the screen position after shaking.
    $ shake_x, shake_y = 0, 0

    return


label phone_rings:
    #loop forever
    while True:
        "Phone rings"
        "Beep! Beep!"

        "Do you want to answer the phone?"

        menu:
            "Yes":
                "You pick up the phone."
                return
            "No":
                "You ignore the phone."

    return 

# The game starts here.
label start:
    # show screen attributes_screen
    # hide screen attributes_screen
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #fade in audio in loop
    play music "city.mp3" loop

    show city_1

    "In the futuristic city of NeoKorpus, advanced cybernetics and AI have become an integral part of society."
    
    show city_3

    " The line between humans and machines blurs as people augment their bodies and minds with technology"

    show city_2

    "The city is a bustling metropolis, filled with people from all walks of life. It is a place of opportunity, but also of danger."

    "Amidst this cybernetic renaissance, a mysterious and dangerous conspiracy is brewing—one that threatens to undermine the very fabric of NeoKorpus."

    #fade out audio
    stop music fadeout 2.0

    show bg_diner

    #fade in
    with dissolve
    "It is a quiet night at the diner. The neon lights outside cast a soft glow on the empty streets."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show alex
    with dissolve
    

    alex "(Muffled) Mmm..."
    alex "This is one huge burger!"

    alex "(Takes another bite and accidentally spills a bit of mustard on the table.)"

    alex "Oops!"
    
    #shake screen
    alex "Okay, I need to eat this thing without making a mess."

    hide alex

    show olivia
    olivia "Hey, Alex!"

    call phone_rings
    # This ends the game.

    return
