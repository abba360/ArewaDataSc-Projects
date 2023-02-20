""" A class to model a user"""
class User_v2:
    '''Attempt to model a user profile'''
    def __init__(self,first_name,last_name,age,city,profession):
        '''initialize user first and last name and other info'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.profession = profession
        self.login_attempts = 0


    def describe_user(self):
        '''Print user profile'''
        print(f'{self.first_name} {self.last_name}, a {self.age} years old {self.profession} lives in {self.city}')

    def greet_user(self):
        '''Print a personalised greeting to specific user'''
        print(f'Good day {self.first_name} {self.last_name}, happy to see you with us')
    
    def increment_login_attempts(self):
        '''Increase the number of login attempts by 1'''
        self.login_attempts += 1

    def reset_login_attempts(self):
        '''Reset the login_attempts back to zero'''
        self.login_attempts = 0
