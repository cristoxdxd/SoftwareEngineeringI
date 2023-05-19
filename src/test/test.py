def validate(ci):
    if len(ci) != 10:
        print("Invalid CI")
        return

    try:
        validator = 0
        for i, digit in enumerate(ci):
            value = int(digit)
            if i % 2 == 0:
                value *= 2
                if value > 9:
                    value -= 9
            validator += value

        if validator % 10 == 0:
            print("Valid CI")
        else:
            print("Invalid CI")
    except ValueError:
        print("Invalid CI")

if __name__ == "__main__":
    ci_number = input("Enter the Ecuadorian CI number: ")
    validate(ci_number)