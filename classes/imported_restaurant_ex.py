"""
9-10. Imported Restaurant: Using your latest Restaurant class, store it in a mod￾ule. Make a separate file that imports Restaurant. Make a Restaurant instance, 
and call one of Restaurant’s methods to show that the import statement is working properly.
"""
from restaurant import Restaurant_v2
asin = Restaurant_v2('Sweeties','Indian') 
asin.describe_restaurant()   # works output=   Sweeties offers the best Indian meals and has served 0 customers so far