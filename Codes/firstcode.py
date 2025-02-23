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
