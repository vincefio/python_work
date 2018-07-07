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

#make an instance of the class
restaurant1 = Restaurant('bitches at work', 'organic')
restaurant2 = Restaurant('coders bay', 'tough food')
restaurant3 = Restaurant('fools good', 'carribean')

#restaurant1.number_served = 3
#restaurant1.set_number_served()
#restaurant1.increment_number_served()
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
'''
