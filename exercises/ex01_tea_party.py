"""Tea party planning that will calculate the amount of tea, treats and cost"""

__author__: str = "730768692"
# author needs TWO underscores on either side
# PID needs quotes around the number because it is defined as a str


def main_planner(guests: int) -> None:
    """Entry point of program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    # must put str before each function call to define the value of the function
    # must make guests=people to assign a value to the variable


def tea_bags(people: int) -> int:
    """Use number of people to calculate number of tea bags needed"""
    return people * 2


def treats(people: int) -> int:
    """Use number of tea bags to calculate number of treats needed"""
    return int(tea_bags(people=people) * 1.5)
    # calls the tea_bags function and uses it's return value


def cost(tea_count: int, treat_count: int) -> float:
    """Use tea bags and treats to calculate the expected cost"""
    return (tea_count * 0.5) + (treat_count * 0.75)
    # tea_count and treat_count do not need to be defined now; defined when called


if __name__ == "__main__":
    # must equal "__main__" not main_planner; main_planner function is called below
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
