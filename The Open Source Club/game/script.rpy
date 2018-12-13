# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character(_("Hana"), color="#c8ffc8")

# This is a variable that is True if you've compared a visual novel to a book
# otherwise

default book = False



# The game starts here.

label start:

    # Start by playing music.
    play music "itty-bitty-8-bit.mp3"

    scene anime-classroom
    with fade

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show hana

    # These display lines of dialogue.

    h "You've created a new Ren'Py game."

    h "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
