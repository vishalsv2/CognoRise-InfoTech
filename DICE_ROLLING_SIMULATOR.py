import random

def roll_dice(num_sides, num_rolls):
    for _ in range(num_rolls):
        print(random.randint(1, num_sides))

num_sides = int(input("Enter the number of sides on the dice: "))
num_rolls = int(input("Enter the number of rolls: "))

roll_dice(num_sides, num_rolls)
