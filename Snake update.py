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
#hello
pygame.mixer.init()
music = pygame.mixer.Sound("Sonic Blaster.mp3")
apple_munch=pygame.mixer.Sound("Minecraft Eating - Sound Effect HD.mp3")
music.set_volume(0.05)
'''NA: Defines music and sound'''

from random import randrange  
from turtle import *       
from freegames import square, vector  

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 18:31:09 2025

@author: andre
"""

import pygame
import sys
   
#Initialize pygame module
pygame.init()

#Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Menu Test")


#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 50, 255)
RED = (255, 50, 50)
GREEN = (0, 128, 0)

#Font
font = pygame.font.SysFont(None, 40)

#Game Title
title_font = pygame.font.SysFont(None, 70)
title_surf = title_font.render("Snake Game", True, WHITE) 
title_rect = title_surf.get_rect(center =(WIDTH / 2, 60))

#Options Screen Title
options_font = pygame.font.SysFont(None, 70)
options_surf = options_font.render("Game Options", True, WHITE) 
options_rect = options_surf.get_rect(center =(WIDTH / 2, 60))

#Speed Options Title
speed_font = pygame.font.SysFont(None, 70)
speed_surf = speed_font.render("Speed Options", True, WHITE) 
speed_rect = speed_surf.get_rect(center =(WIDTH / 2, 60))

#Button Function
def draw_button(text, x, y, width, height, inactive_color, active_color):
    mouse = pygame.mouse.get_pos()
    hovered = x < mouse[0] < x + width and y < mouse[1] < y + height
    
    # Draw rectangle
    color = active_color if hovered else inactive_color
    pygame.draw.rect(screen, color, (x, y, width, height))
    
    # Draw text
    text_surf = font.render(text, True, WHITE)
    text_rect = text_surf.get_rect(center=(x + width/2, y + height/2))
    screen.blit(text_surf, text_rect)
    
    return hovered  # return True if mouse is hovering

#Main Menu Loop

menu_state = "main"

def main_menu():
    global menu_state
    while True:
        screen.fill(BLACK)
        screen.blit(title_surf, title_rect)
        
        # Draw buttons
        play_hover = draw_button("Play", 200, 100, 200, 50, BLUE, GREEN)
        options_hover = draw_button("Options", 200, 200, 200, 50, BLUE, GREEN)
        quit_hover = draw_button("Quit", 200, 300, 200, 50, BLUE, GREEN)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_hover:
                    print("Play clicked")  # Call your game function here
                elif options_hover:
                    menu_state = "options"
                    return  # exit main_menu to switch to options
                elif quit_hover:
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        
def options_menu():
    global menu_state
    while True:
        screen.fill(BLACK)
        screen.blit(options_surf, options_rect)
        
        # Draw buttons
        map_hover = draw_button("Map Size", 200, 100, 200, 50, BLUE, GREEN)
        speed_hover = draw_button("Speed", 200, 200, 200, 50, BLUE, GREEN)
        back_hover = draw_button("Back", 200, 300, 200, 50, BLUE, GREEN)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_hover:
                    menu_state = "main"
                    return  # go back to main menu
                elif map_hover:
                    print("Map Size clicked")
                    menu_state = "map_size"
                    return
                elif speed_hover:
                    print("Speed clicked")
                    menu_state = "speed"
                    return
        pygame.display.update()
        
def speed_menu():
    global menu_state
    while True:
        screen.fill(BLACK)
        screen.blit(speed_surf, speed_rect)
        
        # Draw buttons
        slow_hover = draw_button("Slow", 200, 100, 200, 50, BLUE, GREEN)
        medium_hover = draw_button("Medium", 200, 175, 200, 50, BLUE, GREEN)
        fast_hover = draw_button("Fast", 200, 250, 200, 50, BLUE, GREEN)
        back_hover = draw_button("Back", 200, 325, 200, 50, BLUE, GREEN)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_hover:
                    menu_state = "options"
                    return  # go back to options menu
                elif slow_hover:
                    print("Slow clicked")
                    delay = 200
                    return delay
                elif medium_hover:
                    print("Medium clicked")
                    delay = 100
                    return delay
                elif fast_hover:
                    print("Fast clicked")
                    delay = 50
                    return delay
        
        pygame.display.update()
        
def map_menu():
    global menu_state
    while True:
        screen.fill(BLACK)
        screen.blit(speed_surf, speed_rect)
        
        # Draw buttons
        small_hover = draw_button("Small", 200, 100, 200, 50, BLUE, GREEN)
        medium_hover = draw_button("Medium", 200, 175, 200, 50, BLUE, GREEN)
        large_hover = draw_button("Large", 200, 250, 200, 50, BLUE, GREEN)
        back_hover = draw_button("Back", 200, 325, 200, 50, BLUE, GREEN)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_hover:
                    menu_state = "options"
                    return  # go back to options menu
                elif small_hover:
                    print("Small clicked")
                elif medium_hover:
                    print("Medium_map clicked")
                elif large_hover:
                    print("Large clicked")
        
        pygame.display.update()


while True:
    if menu_state == "main":
        main_menu()
    elif menu_state == "options":
        options_menu()
    elif menu_state == "speed":
        speed_menu()
    elif menu_state == "map_size":
        map_menu()

food = vector(0, 0)  

snake = [vector(10, 0)]

aim = vector(0, -10)

colour_list = ['red','orange','yellow','green','blue','indigo','violet','pink','cyan','black']
snake_colour = 'black'
food_colour = 'red'
'''KL: These variables and the list will be used later to randomize the colour of the food and snake.
'''

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

    global snake_colour
    global food_colour
    '''KL: snake_colour and food_colour are defined outside the function, so the global keyword tells
    the program to use the variables outside the function instead of creating new ones.
    '''
   
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

        snake_colour = food_colour
        food_colour = colour_list[randrange(10)]
        '''KL: Sets the colour of the snake to the old food colour, and randomizes the current colour of the food.
        '''
        
        delay = max(10, delay - 12)
        """ GG Everytime an apple is eaten, the delay is decreased by 12ms. 
        This is within a max function, making the maximum delay 10ms."""
    else:
        snake.pop(0)

    clear()
    for body in snake:
        square(body.x, body.y, 9, snake_colour)
    square(food.x, food.y, 9, food_colour)
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
