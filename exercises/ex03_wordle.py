"""Wordle: Player makes 6 guesses at the secret word and provides an emoji reponse"""

__author__ = "730768692"


def input_guess(secret_word_len: int) -> str:
    """Checks the player's guess is the right length"""
    word: str = input(f"Enter a {secret_word_len} character word: ")
    while len(word) != secret_word_len:
        word = input(f"That wasn't {secret_word_len} chars! Try again: ")
        # Need to redefine the variable word by giving the player another chance
    return word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks if char_guess is found inside secret_word"""
    assert len(char_guess) == 1
    # Assert this assumption such that an error is raised if not true

    index: int = 0
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True

        index += 1
    return False
    # Need to be outside the while loop because the return type is bool


def emojified(guess: str, secret: str) -> str:
    """Use emojis to represent the accuracy of a guess in relation to a secret word"""

    assert len(guess) == len(secret)
    index: int = 0

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    emoji_str: str = ""
    # Need to have an empty str to build emojis

    while index < len(secret):
        if guess[index] == secret[index]:
            emoji_str += GREEN_BOX
        elif contains_char(secret, guess[index]):
            # Contains_char must have parameters when it is called
            emoji_str += YELLOW_BOX
        else:
            emoji_str += WHITE_BOX
        index += 1

    return emoji_str
    # Need this return emoji_str to have the results returned


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1

    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(secret_word_len=len(secret))
        # Need to save return value of input_guess function as a new variable
        # Need to define secret_word_len as the length of secret
        # Need to define before calling
        print(emojified(guess=guess, secret=secret))

        if guess == secret:
            # Before guess was a function (input_guess); needs to be a variable
            print(f"You won in {turns}/6 turns")
            return None
        else:
            turns += 1

    print("X/6 - Sorry, try again tomorrow!")
    return None


if __name__ == "__main__":
    main(secret="codes")
