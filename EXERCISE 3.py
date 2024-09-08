def gallonsToLiters(gallons):
    liters = gallons * 3.78541
    return liters

def main():
    while True:
        gallons = float(input(" Enter volume in gallons(negative value to quit):"))

        if gallons < 0:
            print("Exit the program")
            break

        liters = gallonsToLiters(gallons)

        print(f"{gallons} gallons equal to {liters:.2f} liters.")

if __name__ == "__main__":
    main()
