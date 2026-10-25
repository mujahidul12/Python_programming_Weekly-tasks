DELIMITER = ","


def collectWords() -> str:
    Words = ""

    while True:
        Word = input("Insert word(empty stops): ")

        if Word == "":
            break

        if Words == "":
            Words = Word
        else:
            Words += DELIMITER + Word

    return Words


def analyseWords(PWords: str) -> None:
    if PWords == "":
        print("- 0 Words")
        print("- 0 Characters")
        print("- 0.00 Average word length")
        return None

    Words = PWords.split(DELIMITER)
    WordCount = len(Words)
    CharacterCount = sum(len(Word) for Word in Words)
    Avg = CharacterCount / WordCount

    print(f"- {WordCount} Words")
    print(f"- {CharacterCount} Characters")
    print("- {:.2f} Average word length".format(Avg))


def main() -> None:
    print("Program starting.")

    Words = collectWords()
    analyseWords(Words)

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()