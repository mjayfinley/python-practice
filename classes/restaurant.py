class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + "-" + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " is now open!")


restaurant = Restaurant("Ted's", "Mexican")
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_two = Restaurant("Chilli's", "American")
restaurant_two.describe_restaurant()
restaurant_two.open_restaurant()

restaurant_three = Restaurant("Arby's", "Fast Food")
restaurant_three.describe_restaurant()
restaurant_three.open_restaurant()
