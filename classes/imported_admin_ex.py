"""
9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173). 
Store the classes User, Privileges, and Admin in one module. Create a sepa￾rate file, make an Admin instance, and call show_privileges() to show that 
everything is working correctly.
"""


from admin import Admin_v2
admin_one = Admin_v2('Lukman','Aliyu',35,'Kaduna','Pharmacist')
admin_one.privileges.show_privileges() # worked  output below
'''This admin has the following privileges
-can add post
-can delete post
-can ban user '''