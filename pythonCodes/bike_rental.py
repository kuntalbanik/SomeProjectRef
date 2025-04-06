#
# Bike rental system through a Bike shop
# Show availability of bikes.
# Enter bike qty.
#


# Bike shop class
class BikeShop:
    __cost_per_bike = 25

    def __init__(self, bikes):
        self.__bikes = bikes

    def show_available_bikes(self):
        print("Total Bikes", self.__bikes)

    def order_qty(self, qty):
        if self.__bikes < 1:
            print("No bikes available to book...")
        elif qty <= self.__bikes:
            self.__bikes = self.__bikes - qty
            print(self.__bikes)
            print("Bikes has been booked. Costing $" + str(qty * self.__cost_per_bike))
        else:
            print("Bikes available " + str(self.__bikes))


bike_obj = BikeShop(100)
while True:
    input_data = int(
        input(
            """
    1. Show available bikes
    2. Reserve bikes
    3. Quit
    """
        )
    )
    if input_data == 1:
        bike_obj.show_available_bikes()
    elif input_data == 2:
        bike_qty = int(input("Enter bike qty : "))
        bike_obj.order_qty(bike_qty)
    else:
        break
