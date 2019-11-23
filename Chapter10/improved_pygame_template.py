"""
  This is an improved version of the earlier-created template that defines if __main__
  and places main into a function. This should be used instead of the template from Chapter6.

  Beef Erikson Studios - 2019
"""

import pygame

# Define basic colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def main():
    """ Main function for the game. """
    pygame.init()

    # Program properties
    size = [800, 600]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("My Game")

    # Loop trigger
    done = False

    # Screen update variable
    clock = pygame.time.Clock()

    # ===== Main Program Loop =====
    while not done:
        # EVENT PROCESSING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        # EVENT PROCESSING DONE

        # GAME LOGIC

        # GAME LOGIC DONE

        # DRAW CODE

        screen.fill(WHITE)

        # DRAW CODE DONE

        # Update screen
        pygame.display.flip()

        # 60 FPS
        clock.tick(60)

    # Closes window and quits
    pygame.quit()


if __name__ == "__main__":
    main()
