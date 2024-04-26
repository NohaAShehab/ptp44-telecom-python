
"""
    behaviour --> associated to the class ===> // doesn't depend on instance
"""

# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def generate_default_std(cls):
#         print(cls)
#         return cls('default')
#
# obj=Student.generate_default_std()
# print(obj)


#lambda expression

mylambda = lambda x: x*2
print(mylambda(4))

val = lambda x: x/3
print(val(4))


### map
l = [3,4,5]
# * 5
nums= map(lambda num :num*5, l) # map object
print(nums)
print(list(nums))

# filter
l2 = [3,132,24,22,25,23]
# odd never
odd_nums = filter(lambda num:num%2==1,l2)
print(odd_nums) # filter_obj
print(list(odd_nums))















