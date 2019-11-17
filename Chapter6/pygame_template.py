"""
 Template to use for any blank project.

 Beef Erikson Studios, 2019
"""

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
pygame.display.set_caption('My Game Name')

# Loops until user clicks the close button
done = False

# Manages how fast the screen updates
clock = pygame.time.Clock()

# ----- Main Loop -----
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Drawing code should go here

    # Clear screen to white
    screen.fill(WHITE)

    # Updates screen
    pygame.display.flip()

    # Limits to 60 FPS
    clock.tick(60)

pygame.quit()
