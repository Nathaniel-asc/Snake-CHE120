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
import pygame
'''NA: imports pygame, used for sound design'''

pygame.mixer.init()
music = pygame.mixer.Sound("Sonic Blaster.mp3")
apple_munch=pygame.mixer.Sound("Minecraft Eating - Sound Effect HD.mp3")
music.set_volume(0.05)
'''NA: Defines music and sound'''

from random import randrange  
from turtle import *       
from freegames import square, vector  

food = vector(0, 0)  


snake = [vector(10, 0)]


aim = vector(0, -10)

delay = 100 

""" GG Defines the starting delay as 100ms"""

def change(x, y):
    """This function is responsible for changing the snake's direction."""
    if (aim.x == -x and aim.y == -y):
        return
    '''NA: Stops the snake from reversing direction, instantly killing itself if the snake is longer then 1'''
    aim.x = x

   
    aim.y = y

    

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190
    
def move():
    """Move snake forward one segment."""

    global delay
    
    """ GG Delay is defined outside the function, 
    global allows the delay value to be changed, within the move function."""
    
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        music.stop()
        return
    

    snake.append(head)
    
    if head == food:
        print('Snake:', len(snake))
        apple_munch.play()
        '''NA: plays munch sound if player touches apple'''
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        
        delay = max(10, delay - 12)
        """ GG Everytime an apple is eaten, the delay is decreased by 12ms. 
        This is within a max function, making the maximum delay 10ms."""
    else:
        snake.pop(0)

    clear()
    for body in snake:
        square(body.x, body.y, 9, 'black')
    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, delay)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
music.play()
'''NA: Starts playing the music'''
done()
