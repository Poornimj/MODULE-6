import math

def unitPricePerSquareMeter(diameter, price):
    diameterMeters = diameter / 100
    radiusMeters = diameterMeters / 2

    areaSquareMeters = math.pi * (radiusMeters ** 2)
    unitPrice = price / areaSquareMeters

    return unitPrice

def main():
    diameter1 = float(input("Enter the diameter of the 1st pizza in centimeters:"))
    price1 = float(input("Enter the price of the 1st pizza in euros:"))

    diameter2 = float(input("Enter the diameter of the 2nd pizza in centimeters:"))
    price2 = float(input("Enter the price of the 2nd pizza in euros:"))

    unitPrice1 = unitPricePerSquareMeter(diameter1, price1)
    unitPrice2 = unitPricePerSquareMeter(diameter2, price1)

    print(f"First pizza unit price is: {unitPrice1:.2f} euros per square meter.")
    print(f"Second pizza unit price is: {unitPrice2:.2f} euros per square meter.")

    if unitPrice1 < unitPrice2:
        print("The first pizza provides better value for money.")

    elif unitPrice2 < unitPrice1:
        print("The second pizza provides better value for money.")

    else:
        print("Both Pizzas provide the same value for money.")

main()