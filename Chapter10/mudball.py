"""
  Sample text-only game that demonstrates function usages.
  Players take turns lobbing mudballs at each other until one gets hit.

  Beef Erikson Studios - 2019
"""

import math
import random


def print_instructions():
    """ This function prints the game's instructions. """
    print("""
    Welcome to Mudball! The idea is to hit the other player with a mudball.
    Enter your angle (in degrees) and the amount of PSI to charge your gun with.
    """)


def calculate_distance(psi, angle_in_degrees):
    """ Calculates the distance the mudball will fly. """
    angle_in_radians = math.radians(angle_in_degrees)
    distance = .5 * psi ** 2 * math.sin(angle_in_radians) * math.cos(angle_in_radians)
    return distance


def get_user_input(name):
    """ Gets user input for psi and angle. Returns a list of two numbers """
    psi = float(input(name + " charge the gun with how many psi? "))
    angle = float(input(name + " shoot the gun at what angle? "))
    return psi, angle


def get_player_names():
    """ Gets a lit of player names and how many are playing. """
    print("Enter player names. Enter as many players as you like.")
    done = False
    players = []

    while not done:
        player = input("Enter player name (hit enter to quit entering names): ")
        if len(player) > 0:
            players.append(player)
        else:
            done = True

    print()
    return players


def process_player_turn(player_name, distance_apart):
    """
      This runs the turn for each player.
      If it returns False, keep going with the game.
      If it returns True, someone has won and the game stops.
    """
    psi, angle = get_user_input(player_name)

    distance_mudball = calculate_distance(psi, angle)
    difference = distance_mudball - distance_apart

    if difference > 1:
        print("You were ", difference, " yards too far!")
    elif difference < -1:
        print("You were ", difference * -1, " yards too short!")
    else:
        print("Hit! \n" + player_name + " wins!")
        return True

    print()
    return False


def main():
    """ Main program """

    # Start the game
    print_instructions()
    player_names = get_player_names()
    distance_apart = random.randrange(50, 150)

    # Keep looping until there is a winner
    done = False
    while not done:
        for player_name in player_names:
            done = process_player_turn(player_name, distance_apart)
            if done:
                break


if __name__ == "__main__":
    main()
