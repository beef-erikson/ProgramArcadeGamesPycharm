"""
 Example of using animation in Pygame

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

# Starting position of square to move around
rect_x = 50
rect_y = 50

# Speed of square by value
rect_speed_x = 5
rect_speed_y = 5

# ----- Main Loop -----
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Drawing code should go here

    # Clear screen to white
    screen.fill(BLACK)

    # Draw 50x50 rectangle to bounce around
    pygame.draw.rect(screen, RED, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, WHITE, [rect_x + 10, rect_y + 10, 30, 30])

    # Sets speed of rectangle
    rect_x += rect_speed_x
    rect_y += rect_speed_y

    # Bound object inside window
    if rect_y > 550 or rect_y < 0:
        rect_speed_y *= -1
    if rect_x > 750 or rect_x < 0:
        rect_speed_x *= -1

    # Updates screen
    pygame.display.flip()

    # Limits to 60 FPS
    clock.tick(60)

pygame.quit()
