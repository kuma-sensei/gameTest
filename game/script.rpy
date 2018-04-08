# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define n = Character(what_italic=True, who_color = "#8888bb")


# The game starts here.

label start:
    python:
        n.name = None

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."
    
    n "Is that right? So what's next?"

    e "Once you add a story, pictures, and music, you can release it to the world!"
    
    n "And that's all there is to it?"
    
    e "That's all!"
    
    n "What about defining who I am? How do I get to tell you about me?"
    
    e "Good question. I guess you should check out the documentation!"
    
    # Code segment to get name from user and save it to character n
    label name_incomplete:
    python:
        nname = renpy.input("What is your name?")
        nname = nname.strip()

        if not nname:
            nname = "????"
        n.name = nname
 
    # Place comments around to figure out what each segment does.
    menu:
        "Is the name [nname] correct?"
        "Yes":
            jump name_complete
        "No":
            jump name_incomplete
            
    label name_complete:
    
    n "My name is [nname]!"

    e "Well, I guess that's a start!"
    
    n "And hey, look, I have a name now!"
    
    menu:
        e "Do you identify more closely as a boy or a girl?"
        "Boy":
            python:
                n.gender = "m"
            e "I see, good to know! So we can call you Mr. [n.name] then."
        "Girl":
            python:
                n.gender = "f"
            e "I see, so we can perhaps call you Ms. [n.name]? Got it."
        "Neither":
            python:
                n.gender = "n"
            e "Okay, that's just fine too! We can just call you [n.name]."
    
    e "So I wonder where this journey will take you next? Only time will tell!"
    
    # This ends the game.

    return
