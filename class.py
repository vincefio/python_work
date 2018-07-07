class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Restaurant name is ' + self.restaurant_name + ' and type is ' + self.cuisine_type)

    def open_restaurant(self):
        print('restaurant is open')


#make an instance of the class
restaurant = Restaurant('bitches at work', 'organic')

print(restaurant.restaurant_name + ' ' + restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
