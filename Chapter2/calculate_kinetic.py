# Calculates kinetic energy based on user input

mass = float(input("Enter the object's mass in kilograms: "))
velocity = float(input("Enter the object's speed in meters per second: "))
energy = 0.5 * mass * velocity * velocity

print("the object has " + str(energy) + " joules of energy.")
