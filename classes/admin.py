""" A set of classes that describes users, admins and admin privileges"""
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



class Privileges:
    '''An attempt to model the privileges an admin user profile has'''
    def __init__(self,privileges = ['can add post','can delete post','can ban user']):
        self.privileges = privileges
    def show_privileges(self):
        '''Display the privileges an admin possesses'''
        if self.privileges:
            print(f'\n This admin has the following privileges')
            for item in self.privileges:
                print(f'-{item}')
        else: 
            print(f'This user has no privileges')


class Admin_v2(User_v2):
    '''An attempt to model an Admin, a special kind of User'''
    def __init__(self,first_name,last_name,age,city,profession):
        super().__init__(first_name,last_name,age,city,profession)
        self.privileges = Privileges()