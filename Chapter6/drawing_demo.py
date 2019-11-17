"""
 Drawing Examples

 Show how to draw lines, complex lines using equations, polygons and text.
 Beef Erikson Studios, 2019
"""

import math
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
pygame.display.set_caption('Drawing Demo')

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

    # ----- Drawing code -----

    # Clear screen to white
    screen.fill(WHITE)

    # Draws some lines
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    pygame.draw.line(screen, BLACK, [20, 0], [120, 100], 7)
    pygame.draw.line(screen, RED, [40, 0], [140, 100], 10)

    # Draws several lines using a for loop
    for y_offset in range(100, 250, 10):
        pygame.draw.line(screen, BLUE, [60, 10 + y_offset], [160, 110 + y_offset], 5)

    # Draw more complex things using sine and cosine
    for i in range(200):
        radians_x = i / 20
        radians_y = i / 6

        x = int(75 * math.sin(radians_x)) + 300
        y = int(75 * math.cos(radians_y)) + 100

        pygame.draw.line(screen, BLACK, [x, y], [x + 5, y], 5)

    # Draw multiple X's using multiple elements inside a loop
    for x_offset in range(30, 300, 30):
        pygame.draw.line(screen, BLACK, [x_offset, 400], [x_offset - 10, 390], 2)
        pygame.draw.line(screen, BLACK, [x_offset, 390], [x_offset - 10, 400], 2)

    # Draw an ellipse, using a rectangle for bounds
    pygame.draw.rect(screen, BLACK, [350, 250, 250, 100], 2)
    pygame.draw.ellipse(screen, BLACK, [350, 250, 250, 100], 2)

    # Draws arcs that form an ellipse
    pygame.draw.arc(screen, GREEN, [350, 400, 250, 100], math.pi/2, math.pi, 2)
    pygame.draw.arc(screen, BLACK, [350, 400, 250, 100], 0, math.pi/2, 2)
    pygame.draw.arc(screen, RED, [350, 400, 250, 100], 3*math.pi/2, 2*math.pi, 2)
    pygame.draw.arc(screen, BLUE, [350, 400, 250, 100], math.pi, 3*math.pi/2, 2)

    # Draws triangle using the polygon command
    pygame.draw.polygon(screen, BLUE, [[600, 100], [500, 200], [700, 200]], 5)

    # -- Text
    # Selects font (font name, size, bold, italics)
    font = pygame.font.SysFont('Calibri', 22, False, False)

    # Render the text (text, anti-aliasing, color)
    text = font.render("Here's some words", True, RED)

    # Blits the image on the screen (text, location)
    screen.blit(text, [550, 50])

    # ----- End of Drawing Code -----

    # Updates screen
    pygame.display.flip()

    # Limits to 60 FPS
    clock.tick(60)

pygame.quit()
