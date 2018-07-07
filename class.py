class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Restaurant name is ' + self.restaurant_name + ' and type is ' + self.cuisine_type)

    def open_restaurant(self):
        print('restaurant is open')


#make an instance of the class
restaurant1 = Restaurant('bitches at work', 'organic')
restaurant2 = Restaurant('coders bay', 'tough food')
restaurant3 = Restaurant('fools good', 'carribean')

'''
print(restaurant.restaurant_name + ' ' + restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
'''

'''
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
'''
class User():
    def __init__(self, first_name, last_name, interest):
        self.first_name = first_name
        self.last_name = last_name
        self.interest = interest
    def describe_user(self):
        print('First name is ' + self.first_name)
        print('Last name is ' + self.last_name)
        print('User interest is ' + self.interest)

vince = User('Vince', 'Fiorilli', 'coding')

vince.describe_user()
