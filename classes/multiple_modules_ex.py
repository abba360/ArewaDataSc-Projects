from admin_privileges import Admin

superior = Admin('Kamil','Tahir',40,'Kano','Student')
superior.show_privileges()  # worked, output below
""" 
This admin has the following privileges
-can add post
-can delete post
-can ban user
"""