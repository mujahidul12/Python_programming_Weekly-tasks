def askName() -> str:
    Name = input("Insert name: ")
    return Name


def greetUser(PName: str) -> None:
    print(f"Hello {PName}!")
    return None


def main() -> None:
    print("Program starting.")
    Name = askName()
    greetUser(Name)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
