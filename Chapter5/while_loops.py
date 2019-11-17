# Print 0 to 9
i = 0
while i < 10:
    print(i)
    i += 1

# ^ That would be the same as:
for i in range(10):
    print(i)

# Usually while loop is used for a way to escape block of code.
user_quit = "n"
while user_quit == "n":
    user_quit = input('Do you want to quit? ')

# Another way is with a bool
done = False
while not done:
    user_quit = input('Do you want to quit? ')
    if user_quit == 'y':
        done = True

    attack = input('Does your elf attack the dragon? ')
    if attack == 'y':
        print('Bad choice, you died.')
        done = True
