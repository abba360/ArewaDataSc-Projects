""" A class that can be used to represent a restaurant"""

class Restaurant_v2:
    '''Another attempt to model a restaurant'''
    def __init__(self,restaurant_name,cuisine_type):
        '''Initialise restaurant name and cuisine type'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''Print restaurant name and cuisine type'''
        print(f'{self.restaurant_name} offers the best {self.cuisine_type} meals and has served {self.number_served} customers so far')

    def open_restaurant(self):
        '''Indicate that restaurant is open'''
        print(f'{self.restaurant_name} is open for business')
    
    def set_number_served(self,num):
        '''Set the number of customers that have been served'''
        if num >= self.number_served:
            self.number_served = num
        else:
            print('We only move forward!!')

    def increment_number_served(self,add):
        '''Increase the number of customers served by an amount'''
        if add > 0:
            self.number_served += add
        else:
            print('Customers served can\'t be reduced')
