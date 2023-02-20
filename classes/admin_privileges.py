"""A set of classes to model and admin and privileges that the admin can have"""
from user import User_v2
class Admin(User_v2):
    '''An attempt to model an Admin, a special kind of User'''
    def __init__(self,first_name,last_name,age,city,profession):
        super().__init__(first_name,last_name,age,city,profession)
        self.privileges = ['can add post','can delete post','can ban user']
    def show_privileges(self):
        '''Display the privileges an admin possesses'''
        print(f'\n This admin has the following privileges')
        for item in self.privileges:
            print(f'-{item}')

his_admin = Admin('Lukman','Aliyu',28,'Kaduna','Pharmacist')
his_admin.show_privileges()


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
