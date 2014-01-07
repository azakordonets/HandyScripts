# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math
# initialize global variables used in your code
num_range = 100
value = None
attemps = None
win = False
rangeState = True

# helper function to start and restart the game
def defineRange():
    global rangeState
    if rangeState:
        range100()
    else:
        range1000()

def new_game():
    global attemps
    global win
    if attemps == 0:
        if win:
            print "Win!"
            win = False
            defineRange()
        else:
            print "Looser"
            defineRange()

    # remove this when you add your code
    pass


# define event handlers for control panel
def range100():
    global num_range
    global value
    global attemps
    global rangeState
    rangeState = True
    attemps = 3
    value = random.randrange(0, num_range)
    print value
    return value

    # remove this when you add your code
    pass

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    global value
    global attemps
    global rangeState
    rangeState = False
    attemps = 10
    num_range = num_range * 10
    value = random.randrange(0, num_range)
    return value
    # remove this when you add your code
    pass

def input_guess(guess):
    # main game logic goes here
    guess = int(guess)
    global attemps
    if guess < value:
        print "Higher!"
        attemps-=1
        print "Atempts " + str(attemps)
        new_game()
    elif guess> value:
        print "Lower!"
        attemps-=1
        print "Atempts " + str(attemps)
        new_game()
    else:
        print "Correct!"
        global win
        global atemps
        atemps = 0
        win = True
        new_game()
    # remove this when you add your code



# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter the number",input_guess , 200)

new_game()

# register event handlers for control elements



# call new_game and start frame
frame.start()


# always remember to check your completed program against the grading rubric