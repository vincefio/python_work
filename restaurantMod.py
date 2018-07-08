class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('Restaurant name is ' + self.restaurant_name + ' and type is ' + self.cuisine_type)

    def open_restaurant(self):
        print('restaurant is open')

    def set_number_served(self):
        newNum = input('how many have been served?')
        self.number_served = newNum
        print('new number served is ' + str(newNum))

    def increment_number_served(self):
        self.number_served += 1
        print('number served incresed.  now ' + str(self.number_served))
