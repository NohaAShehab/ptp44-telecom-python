"""
    any .py file ---> is considered a module.
    module - -> can be imported /// import part of it
"""

course = "python"

def saywelcome():
    print("Welcome to python modules")


print(course)
saywelcome()

""" every python modules has its entry point 
--> for main 
__name__ ='__main__'
"""


"plz run this code only if the python_modules is running otherwise no "
if __name__ == "__main__":
    print("--- this is running in python_modules only ----")