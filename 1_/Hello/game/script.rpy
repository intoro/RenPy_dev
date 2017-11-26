# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mom = Character("Mommy", color="#e100ff")
define mad = Character("Madeline", color="#ffcccc")
define alex = Character("Alex dog", color="#03c6fe")

# The game starts here.

label start:

    play music "Samurai's Rainy Day.mp3"

    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    scene bg sunset_1
    show maddy listen at left

    # These display lines of dialogue.
    "It's a beautiful sunny morning"

    mom "You're amazing Madeline."

    scene bg sunset_2
    with fade

    mom "Once you eat your breakfast we can explore the world!"

    mad "It is a wonderful day"

    scene maddy watch
    show alex listen at right

    alex "woof woof"

    scene bg maddalex


    mom "Don't worry, You are coming too!"
    scene bg sunset_3
    with fade

    mad "I Love You Mommy!!"

    # This ends the game.

    return
