from restaurantMod import Restaurant

from random import randint


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

class User():
    def __init__(self, first_name, last_name, interest):
        self.first_name = first_name
        self.last_name = last_name
        self.interest = interest
        self.login_attempts = 0
    def describe_user(self):
        print('First name is ' + self.first_name)
        print('Last name is ' + self.last_name)
        print('User interest is ' + self.interest)
    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts
    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts

vince = User('Vince', 'Fiorilli', 'coding')

#vince.describe_user()
'''
print(vince.increment_login_attempts())
print(vince.increment_login_attempts())
print(vince.increment_login_attempts())
print(vince.reset_login_attempts())
'''

#working with inheritence
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']
    def display_flavors(self):
        for flavor in self.flavors:
            print('flavors we have: ' + flavor)

my_stand = IceCreamStand('vinces fudge pops', 'ice cream')
#my_stand.display_flavors()
class Privilege():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    def show_privileges(self):
        for privilege in self.privileges:
            print('user priilege: ' + privilege)
    def add_privilege(self):
        self.privileges.append('new')

#admin class
class Admin(User):
    def __init__(self, first_name, last_name, interest):
        super().__init__(first_name, last_name, interest)
        self.privileges = Privilege()


admin = Admin('johnny', 'utah', 'football')
'''
admin.privileges.add_privilege()
admin.privileges.show_privileges()
'''
class Die():
    def __init__(self):
        self.sides = 6
    def roll_die(self):
        currentNum = 0
        while currentNum < 10:
            x = randint(1, 6)
            print('random number is ' + str(x))
            currentNum += 1

six = Die()
six.roll_die()
