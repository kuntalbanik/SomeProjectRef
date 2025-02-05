#
# Bike rental system through a Bike shop
# Show availability of bikes.
# Enter bike qty.
#


# Bike shop class
class BikeShop:
    __avail_bikes = 100
    __cost_per_bike = 25

    def __init__(self):
        pass

    def show_available_bikes(self):
        print(self.__avail_bikes)

    def order_qty(self, qty):
        if self.__avail_bikes < 1:
            print("No bikes available to book...")
        elif qty <= self.__avail_bikes:
            print("elif block")
            self.__avail_bikes = self.__avail_bikes - qty
            print("Bikes has been booked. Costing $" + str(qty * self.__cost_per_bike))
        else:
            print("Our available qty 100")


while True:
    bike_obj = BikeShop()
    option_string = """
    1. Show available bikes
    2. Reserve bikes
    3. Quit
    """
    print(option_string)
    input_data = int(input("Enter option within range"))
    if input_data == 1:
        bike_obj.show_available_bikes()
    if input_data == 2:
        bike_qty = input("Enter bike qty : ")
        bike_obj.order_qty(bike_qty)
    if input_data == 3:
        break
    else:
        print("Option not available")
