__author__ = "730768692"


def mimic(message: str) -> str:
    """Take imput and repeat it back."""
    return message


def main() -> None:
    """Pull together other functions into main function."""
    print(mimic(message=input("What is your message")))


if __name__ == "__main__":
    main()
