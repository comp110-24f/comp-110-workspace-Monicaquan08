"""Practice with dictionary functions"""

___author___ = "730768692"


def invert(inp: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values"""

    result: dict[str, str] = {}
    # Set up empty dict to add to

    for elem in inp:
        # Iterates through keys
        result[inp[elem]] = elem
        # Set value = key

    test: list[str] = []
    # Set up empty list to check for KeyError because keys cannot repeat

    for elem in inp:
        test.append(inp[elem])
        # Add values from inp to test list

    for idx in range(1, len(test)):
        # Loop through test to check for duplicates

        first: str = test[idx - 1]
        # first item in list; use to compare against the rest of the values

        if test[idx] == first:
            raise KeyError("KeyError")

    return result


def favorite_color(inp: dict[str, str]) -> str:
    """Determines which color is most popular"""

    count_dict: dict[str, int] = {}
    # Dict to store color and number of occurences for each color
    count: int = 1
    # Number of occurence for color

    for name in inp:
        color: str = inp[name]
        if color in count_dict:
            count_dict[color] = count + 1
            # Checks if the color is already in dict; if so it increases count by 1

        else:
            count_dict[color] = count
            # If its a new color; it gets added to the dict

    frequent_color: str = ""
    max_count: int = 0
    # Starting color count to compare against other color counts

    for color_type in count_dict:
        # Loops through each color
        color_count: int = count_dict[color_type]
        # Occurences of color in dict
        if color_count > max_count:
            max_count = color_count
            # If current count of color is greater than max_count; becomes new max_count
            frequent_color = color_type

    return frequent_color


def count(inp: list[str]) -> dict[str, int]:
    """Count the number of times a str appeared in a list"""

    result: dict[str, int] = {}
    # Empty dict to add to

    for elem in inp:

        if elem in result:
            result[elem] += 1
            # If the item already exists in the dict; increase the count by 1
        else:
            result[elem] = 1
            # If the item is NOT already in the dict; add it and makes its count 1

    return result


def alphabetizer(inp: list[str]) -> dict[str, list[str]]:
    """Returns letter and all instances of words that start with that letter"""

    result: dict[str, list[str]] = {}
    # Create an empty dict to add to

    for word in inp:

        first_letter = word[0].lower()
        # Create a variable for the first letter in the word and make it lowercase

        if first_letter not in result:
            result[first_letter] = []
            # If the letter is NOT in the results dict yet; add it with an empty list

        result[first_letter].append(word)
        # Append the word to the list

    return result


def update_attendance(
    attendance_dict: dict[str, list[str]], day: str, student: str
) -> None:

    if day not in attendance_dict:
        attendance_dict[day] = []
        # If day is NOT in attendance_dict; add it with an empty list

    if student not in attendance_dict[day]:
        attendance_dict[day].append(student)
    # If student is NOT already in attendance_dict values; append student
