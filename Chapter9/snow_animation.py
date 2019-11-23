"""
  Creates a 'snow falling' effect with Pygame's animation

  Beef Erikson Studios - 2019
"""
import random

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initializes pygame
pygame.init()

# Open a window at 800x600 resolution
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Snow Animation')

# Loops until user clicks the close button
done = False

# Manages how fast the screen updates
clock = pygame.time.Clock()

# Sets the range of snow
snow_list = []
for i in range(50):
    x = random.randrange(0, 800)
    y = random.randrange(0, 600)
    snow_list.append([x, y])

# ----- Main Loop -----
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Drawing code should go here

    # Black background
    screen.fill(BLACK)

    # Draws the 'snow' defined before the game loop
    for i in range(len(snow_list)):
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
        snow_list[i][1] += 1

        # If the snowflake has moved off the screen, spawn another
        if snow_list[i][1] > 600:
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            x = random.randrange(0, 800)
            snow_list[i][0] = x

    # Updates screen
    pygame.display.flip()

    # Limits to 60 FPS
    clock.tick(60)

pygame.quit()
