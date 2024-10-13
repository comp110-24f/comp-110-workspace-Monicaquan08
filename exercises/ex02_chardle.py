"""EX02 - Chardle - A cute step toward Wordle."""


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")

    if len(word) == 5:
        return word
        # Must be return, not print (so it returns a value that can be used later)
    else:
        print("Error: Word must contain 5 characters.")
        exit()
        # Exit after print but before return (don't want any value to be returned)
        return word


def input_letter() -> str:
    letter: str = input("Enter a single character: ")

    if len(letter) == 1:
        return letter
        # Must be return, not print (so it returns a value that can be used later)
    else:
        print("Error: Character must be a single character.")
        exit()
        # Exit after print but before return (don't want any value to be returned)
        return letter


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)

    count: int = 0
    # Counts the number of matching character

    if word[0] == letter:
        print(letter + " found at index 0")
        count += 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count += 1
    # Can use a while loop to iterate through a str

    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)
    # count must be defined in contains_char func, local variable doesn't exist outside


def main() -> None:
    # Entry point of program; calls other funtions
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
