"""
Functions:
---------

It's all about data transforming, ideally it should:
'take something -> give something"

"""

import shutil


def greeter(name: str) -> None:
    """Greets Zortan"""
    print(f"Zola {name}")


def main() -> None:
    freinds = ["Cece", "Roko", "Chiko", "John", "Ziko"]
    for friend in freinds:
        greeter(friend)


# Invoke the main function
# main()


"""
Better version of greeter function

"""


def greeter(name: str) -> str:
    """Greets Zortan"""
    return f"Zola {name}"


def main() -> None:
    freinds = ["Cece", "Roko", "Chiko", "John", "Ziko"]
    for friend in freinds:
        if "Chiko" in greeter(friend):
            print(f"{friend} is cute")
        else:
            print(greeter(friend))


main()
