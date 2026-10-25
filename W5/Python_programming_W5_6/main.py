def showOptions() -> None:
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None


def askChoice() -> int:
    Choice = input("Your choice: ")

    if Choice.isnumeric():
        return int(Choice)
    else:
        print("Unknown option!")
        return -1


def main() -> None:
    print("Program starting.")

    Count = 0

    while True:
        showOptions()
        Choice = askChoice()

        if Choice == 1:
            print(f"Current count - {Count}")
            print()
        elif Choice == 2:
            Count += 1
            print()
        elif Choice == 3:
            Count = 0
            print()
        elif Choice == 0:
            print("Exiting program.")
            break
        elif Choice != -1:
            print("Unknown option!")
            print()

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()