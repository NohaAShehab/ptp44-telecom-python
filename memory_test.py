

# class Person:
#     pass
#
# p = Person()
# print(isinstance(p, object))



""" inheritance"""
class Person:
    objects = []
    def __init__(self, name):
        print("I am a person")
        self.name = name
        Person.objects.append(self)
    def print_name(self):
        print(f"My name is {self.name}")

class Student(Person):
    def __init__(self, name,email):
        # call parent constructor
        super().__init__(name)
        self.email = email
        print("I am a Student")

s= Student("dd","<EMAIL>")
print(s)
print("--------------------------------")

p = Person("John")

print(Person.objects)



"""
    class A{}
    class B extends A{}
    # reference type
    A obj = new B()  # define instance reference type 
    
    B obj2 = new A() 

    int x = 0;
    in python
    x  =0   # python interpreter detect variable type in the runtime 
"""






