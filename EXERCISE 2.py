import random

def rollDice(sides):
    return random.randint(1,sides)

def main():
    sides = int(input("Enter the number of sides on the dice:"))
    rollResult = 0
    while rollResult != sides:
        rollResult = rollDice(sides)
        print(f"Result of each rolled: {rollResult}")

main()
