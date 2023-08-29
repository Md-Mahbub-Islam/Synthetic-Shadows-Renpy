# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define alex = Character("Alex", color="#ae10a9", image="alex")
define olivia = Character("Olivia", color="#02a474", image="olivia")
define mia = Character("Mia", color="#a90202", image="mia")
define viktor = Character("Viktor", color="#a90202", image="viktor")


# images
image bg_diner = "bg/diner.png"
image city_1 = "bg/city_1.png"
image city_2 = "bg/city_2.png"
image city_3 = "bg/city_3.png"
image lab = "bg/lab.png"
image street_1 = "bg/street_1.png"


# character images
image alex = "ch/alex.png"
image side alex:
    im.FactorScale("ch/side_alex.png", 0.5, 0.5)

image olivia = "ch/olivia.png"
image side olivia:
    im.FactorScale("ch/side_olivia.png", 0.5, 0.5)

image mia = "ch/mia.png"
image side mia:
    im.FactorScale("ch/side_mia.png", 0.5, 0.5)

image viktor = "ch/viktor.png"
image side viktor:
    im.FactorScale("ch/side_viktor.png", 0.5, 0.5)



init python:
    # Define attributes and set initial values
    money = 20
    trust = 50
    morality = 50

    health = 100
    attack = 10
    defense = 10



    bill = 10


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

    voice "voice/desc_in_the_futuristic.mp3"
    "In the futuristic city of NeoKorpus, advanced cybernetics and AI have become an integral part of society."
    
    show city_3

    voice "voice/desc_the_line_between.mp3"
    " The line between humans and machines blurs as people augment their bodies and minds with technology"

    show city_2
    voice "voice/desc_the_city.mp3"
    "The city is a bustling metropolis, filled with people from all walks of life. It is a place of opportunity, but also of danger."

    voice "voice/desc_amidst_this.mp3"
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
    
    voice "voice/alex_mmm.mp3"
    alex "(Muffled) Mmm..."

    voice "voice/alex_this_is_one.mp3"
    alex "This is one huge burger!"


    alex "(Takes another bite and accidentally spills a bit of mustard on the table.)"

    voice "voice/alex_opps.mp3"
    alex "Oops!"
    
    #shake screen
    voice "voice/alex_ok_i_need_to_eat.mp3"
    alex "Okay, I need to eat this thing without making a mess."

    hide alex

    

    call phone_rings
    # This ends the game.


    voice "voice/olivia_hey_alex_how.mp3"
    olivia "Hey, Alex! How's it going?"

    voice "voice/alex_oh_hey_olivia.mp3"
    alex "Oh, hey Olivia! I'm just having dinner at the diner."

    voice "voice/olivia_oh_thats_nice.mp3"
    olivia "Oh, that's nice. Listen, I need your help with something."

    voice "voice/alex_sure_what_is_it.mp3"
    alex "Sure, what is it?"

    voice "voice/olivia_i_am_at_the.mp3"
    olivia "I'm at the lab right now, and I need you to come over and help me with something."

    voice "voice/alex_is_everything_ok.mp3"
    alex "Is everything okay? You sound a bit stressed."

    voice "voice/olivia_well_i_am_not_sure.mp3"
    olivia "Well, I'm not sure. I will tell you more when you get here."

    voice "voice/alex_ok_i_will_be_there.mp3"
    alex "Okay, I'll be there in a bit."

    voice "voice/olivia_thanks_alex.mp3"
    olivia "Thanks, Alex. See you soon."



    #fade out

    "(Hangs up the phone)"

    show alex
    alex "I wonder what's going on."
    hide alex

    show mia
    # mia is a waitress at the diner
    mia "Here is your bill, ma'am."

    show screen attributes_screen

    

    menu:
        "It's [bill] dollars."
        "Pay the bill":
            # If the player has enough money, continue the game.
            $ money -= 10
            "You pay the bill"

        "Haggle (Roll >=10)":
            $ random_roll = renpy.random.randint(1, 20)
            "You roll a [random_roll]."
            
            if random_roll >= 10:
                $ bill = 5
                $ money -= bill

                "You successfully haggle. The bill is now [bill] dollars."
                $ renpy.notify("You successfully haggle.")
            else:
                "You fail to haggle. And pay full price"
                $ money -= bill
                $ renpy.notify("You fail to haggle.")


    mia "Thank you for your business. Have a nice day!"
    hide mia


    # The game continues here.

    alex "I need to get to the lab as soon as possible."

    jump streets
    # This ends the game.
    

    return



label streets:

    "this is the streets"

    return
