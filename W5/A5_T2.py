def frameWord(PWord: str) -> None:
    print("*" * (len(PWord) + 4))
    print("* " + PWord + " *")
    print("*" * (len(PWord) + 4))
    return None


def main() -> None:
    print("Program starting.")
    print()
    Word = input("Insert word: ")
    print()
    frameWord(Word)
    print()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
