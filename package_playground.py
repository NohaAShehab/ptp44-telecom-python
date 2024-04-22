
"import module from package"

# import telecom.inputs
#
# res = telecom.inputs.askforInt("please enter salary: ")
# print(res)

""" alias name"""
# import telecom.inputs as tinputs
# res=tinputs.askforInt(
#     "Please enter a number between 1 and 100")
# print(res)
"""import part of module from package"""
# from telecom.inputs import  askforInt
# print(askforInt())

import iti

iti.sayhello()  # calling function using package name

# from iti.validate_module import  validate_number
# print(validate_number("kfjdh"))

from iti import  validate_number
print(validate_number("rkefhs"))