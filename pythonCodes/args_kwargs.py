"""
Variable & keyword arguments:
-----------------------------
When we don't know how many arguments we are going to receive, we can handle
situation by using variable & keyword argumants syntax.


1. Upnpacking 



"""

# ---------------------------------------------

fname, lname = ("Louis", "Zappa")
print(fname, lname)

first, *rest = ["Cece", "Roko", "John", "Niko"]
print(first)
print(rest)

specs = {"type": "dynamic", "optional": "static typing", "found": "everyware"}
lang = {"name": "Python", **specs}
print(lang)

# --------------------------- Variable arguments ----------------


def unknown_friends(*args: str) -> None:
    for friend in args:
        print(friend)


unknown_friends("Cece", "Roko", "John", "Niko")

# --------------------------- Keyward arguments ----------------


def unknown_product(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")


products = unknown_product(name="pizza", price=3.99, extra_cheese=True)
