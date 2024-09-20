"""Practice using a while loop to iterate over a str"""

__author__ = "730768692"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0

    while index < len(phrase):
        current_char: str = phrase[index]
        # local variable current_char needs to be INSIDE while loop for index to change

        if current_char == search_char:
            count = count + 1
            index = index + 1
        else:
            index = index + 1

    return count
    # needs to return count (an int); do not put print here


print(num_instances(phrase="hi", search_char="h"))
# put print here, so the whole function is being run and the return is being printed
