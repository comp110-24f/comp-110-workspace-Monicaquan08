"""Number guessing game"""

___author___ = "730768692"
# PID needs to be a string


def guess_a_number() -> None:
    secret: int = 7
    x: int = int(input("Guess a number: "))
    # Input comes back as a str, need to convert it to an int
    print("Your guess was " + str(x))
    # Need to make (x) a str to make it compataible with the "+" when printing
    if x == (secret):
        print("You got it!")
    elif x < (secret):
        print("Your guess was too low! The secret number is " + str(secret))
    elif x > (secret):
        print("Your guess was too high! The secret number is " + str(secret))


if __name__ == "__main__":
    guess_a_number()
