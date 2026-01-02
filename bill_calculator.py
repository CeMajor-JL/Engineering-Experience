def calculate_total_per_person(bill, tip_percent, people):
    """
    Calculate how much each person should pay including tip.
    """
    tip_amount = bill * (tip_percent / 100)
    total_bill = bill + tip_amount
    return total_bill / people


def main():
    print("=== Bill Split Calculator ===")

    try:
        bill = float(input("Enter bill amount: "))
        tip_percent = float(input("Enter tip percentage: "))
        people = int(input("Number of people splitting the bill: "))

        if bill <= 0 or tip_percent < 0 or people <= 0:
            print("Values must be greater than zero.")
            return

        per_person = calculate_total_per_person(bill, tip_percent, people)
        print(f"Each person pays: ${per_person:.2f}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except EOFError:
        print("Input not provided.")


if __name__ == "__main__":
    main()