def removeOddNum(numbers):
    evenNum = [num for num in numbers if num % 2 == 0]
    return evenNum

def main():
    originalList = [12,13,14,15,16,17,18,19,20]

    evenList = removeOddNum(originalList)

    print(f"List Of Original: {originalList}")
    print(f"List which odd numbers removed: {evenList}")

main()
