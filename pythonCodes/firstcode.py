print("Hello World")
print("Another print")

fav_color = input("Enter your favorite color : ").lower()

match fav_color:
    case "green":
        print(f"your favorite color is {fav_color}")
    case "black":
        print(f"your favorite color is {fav_color}")
    case _:
        print(f"Your favorite color is not matched with our system")


STYLEUPPERCASE = "Don't want to change"


"""
ENUM:

This is a very good data structure for creating choices
"""
from enum import Enum, auto


class PizzaSize(Enum):
    SMALL = 8
    MEDIUM = 10
    LARGE = 12


choice = PizzaSize.MEDIUM
print(f"One order for {choice.value} inch pizza")


class Colors(Enum):
    """T-Shirts Verieties"""

    RED = "red"
    BLUE = "blue"
    GREEN = "green"


print(f"One order for {Colors.GREEN.value} T-shirt")


class Role(Enum):
    ASSOCIATE = auto()  # Automatically set to 1
    SUPERVISOR = auto()  # Automatically set to 2
    MANAGER = auto()  # Automatically set to 3


print(Role.SUPERVISOR.value)
