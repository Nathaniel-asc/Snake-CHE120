# -*- coding: utf-8 -*-
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

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
