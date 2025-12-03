#Github user name: Nathaniel-asc

#Nathaniel Ascenzi, NA.
#Zachary Andrews, ZA.
#George Gall, GG.
#Konrad Li, KL.
"""
Created on Thu Nov 27 17:07:03 2025

@author: ndasc
"""

"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange  

"""GG This line of code imports the randrange function from the random module. 
The randrange function is used to generate a random integer from a specified range."""

from turtle import *       

"""GG This line of code brings all all functions, variables and 
classes defined within the turtle module into the namespace."""

from freegames import square, vector  

"""GG This line of code imports the square and vector functions, from the freegames module. 
   The square function draws a square on screen, while the vector function creates a two dimensional vector obejct, (x, y), 
   representing a position through coordinates.""" 

food = vector(0, 0)  

"""GG This line of code assignes the variable name food with a position of (0,0), using the imported vector function to assign the starting spawn point of the first apple. """

snake = [vector(10, 0)]

"""GG This line of code assigns the variable name snake, with the vector position (10,0), this is the starting position of the snake.
This is within a list, as this piece of code represents the snakes head and thus later the rest of the sankes body will be added to this collection.""" 

aim = vector(0, -10)

""" GG this line of code describes the original direction the snake is moving. It assigns the variable aim with the vector (0, -10) or downwards."""


def change(x, y):
    """This function is responsible for changing the snake's direction."""
    aim.x = x

    """GG This line of code changes the direction of the snake in the horizontal direction, updating the aim vector in the horizontal direction, to the value of x. 
   This allows only the horizontal direction of the snake to be changed, without affecting the vertical direction."""
    
    aim.y = y

    """GG This line of code changes the direction of the snake in the vertical direction, updating the aim vector in the vertical direction, to the value of y. 
   This allows only the vertical direction of the snake to be changed, without affecting the horizontal direction."""

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190
    '''
    ZA: This function "inside" checks if the snakes head is within both
    the defined X boundaries (in this case, -200 to +190) and Y boundaries
    (-200 to +190) based on the variables "head.x" and "head.y" which
    represent the (x,y) coordinates of the snakes head at any given moment.
    The 'and' statement allows the function to return 'False' if the head
    is outside of either of these boundaries. For example, if 'head.x' =
    200 and 'head.y' = 150, the function will return "False", since it will 
    result in a check of "False and True", which is "False"
    '''

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
    '''
    ZA: First, the variable "head = snake[-1].copy()" essentially takes 
    the most recent value from the list of vectors "snake", and assigns
    that to where the head is at that moment. the method ".copy" allows for
    when trying to move the head forward, instead of overwriting the old 
    position of the head, it will intorudce a new one. I.e. it copies the
    value of the coordinate at that time to allow it to be modified without 
    modifying the original.
    Second, "head.move(aim)" takes the position vector "head" and moves it 
    one step in the direction of aim. For example, suppose head is defined as
    (10,0) and aim is (0,10), then the new head is (10,10).
    Finally, the if statement 'if not inside(head) or head in snake:' is a
    check to determine if the player has lost or not by checking if the player
    is still within the games boundaries (not inside(head)), and also checking 
    if the head has ran into the body of the snake (head in snake). If either of
    these are true, then the square on the board that is occupied by the 
    snake's head (of size 9) is filled with the color red, indicating the player
    has lost. "update()" allows for a refresh of the screen to register the
    previous change. Finally, the "Return" ends the move function, no longer
    allowing the player to move (they lost)
    ''' 

    snake.append(head)
    '''KL: Snake.append(head) adds the value of head, which in this case
    is a copy of the last item in the snake list, to the end of the snake list. 
    The list snake stores the location of each segment of the snake's body, and when 
    the player inputs a new direction, this code segment makes the value stored 
    in head the new head of the snake.
    '''
    if head == food:
        '''KL: This if block checks if the head of the snake is curently
        on a food block. If so, the program prints the current length of the
        snake and sets the food to a random new location
        '''
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        '''KL: snake.pop(0) removes the first item in the snake list. This is because
        to simulate the illusion of movement, the snake increases its length by one
        every time interval, then immediately deletes the tail segment, unless the 
        snake eats the food, in which case the tail doesn't get deleted, increasing
        the snake's length by 1. In this case, the snake's head isn't on a piece of food,
        which is why the snake's length gets decreased by 1, back to its original size
        '''
        snake.pop(0)

    clear()
    '''KL: This line clears the screen, and the following lines of code 
    redraws the snake.
    '''
    for body in snake:
        square(body.x, body.y, 9, 'black')
    '''KL: This for loop runs for every current segment of the snake, which 
    is represented by every item in the snake list. For every segment, the 
    program creates a black square of size 9 at the position of each segment. 
    This displays the snake at its new position.
    '''

    square(food.x, food.y, 9, 'green')
    '''KL: This code makes a green square of size 9 where the food is currently
    located. This ensures the food is redrawn every time the move function is called.
    '''
    update()
    '''KL: update() manually refreshes the screen and displays it all simultaneously.
    This makes the animation look smoother.
    '''
    ontimer(move, 100)
    '''KL: The ontimer function runs a given function after a certain interval
    of time. In this case, the ontimer function runs the move method every 
    100 miliseconds. This is responsible for looping the move method, 
    which is what makes the game run.
    '''

setup(420, 420, 370, 0)
'''NA:
Setup creates a window with size 420 pixles by 420 pixels, with a starting location 370 pixels to the right and 0 pixels down
from the top left of the display'''
hideturtle()
'''NA:
The turtle module usually has a cursor which points to the most recent added visual, hideturtle() removes that cursor '''
tracer(False)
'''NA:
The turtle module usually draws visual elements one at a time, but tracer(False) stops this and makes the entire screen
update at once'''
listen()
'''NA:
The listen function allows the graphics window to recieve inputs from the users keyboard'''
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
'''NA:
The onkey function allows a certain action to happen when keys are pressed.
In this case, when the user presses a direction key, the change function is called, and changes the direction of
the snake'''
move()
'''NA:
Calls the move function to move the snake one segmant'''
done()
'''NA:
Keeps the interactive window open, listening for keyboard events, and the code looping.'''
