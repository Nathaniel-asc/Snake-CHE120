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

"""GG This line of code assigns the variable name snake, with the vector position (10,0). 
This is within a list, as this piece of code represents the snakes head and thus later the rest of the sankes body will be added to this collection.""" 

aim = vector(0, -10)

""" GG this line of code describes the original direction the snake is moving. It assigns the variable aim with the vector (0, -10) or downwards."""


def change(x, y):
    """Change snake direction."""
    aim.x = x

"""GG This line of code changes the direction of the snake in the horizontal direction, updating the aim vector in the horizontal direction, to the value of x."""
    
    aim.y = y

"""GG This line of code changes the direction of the snake in the vertical direction, updating the aim vector in the vertical direction, to the value of y."""

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

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
