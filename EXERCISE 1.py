import random
def rollDice():
    return random.randint(1,6)

def main():
    rollResult = 0

    while rollResult != 6:
        rollResult = rollDice()
        print(f"Result of each rolled: {rollResult}")

if __name__ == "__main__":
    main()
