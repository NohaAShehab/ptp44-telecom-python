""" syntax error must be solved """
# print('iti')
#
# name = "ahmed"
#
# print('test'
#
# print("abc")






""" runtime error ? """
# print("test")
# print(name)
# print("----------------------")


""" logical error """

# def sumnum(num1 ,num2):
#     return num1 + num2
#
# print(sumnum(1,2))  # accurate
# print(sumnum("iti","telecom")) # logical error
# # must be solved by the developer
# print(sumnum(1,"iti")) # run time error



#######################################################


# print("itit")
# exit(9)
# print("978yhkdnd")
# print("abc")


# while True:
#     choice= input("Enter choice l for login , e for exit, r for create: ")
#     if choice == 'l':
#         print("-- loginnnn")
#     elif choice == 'r':
#         print("register")
#     elif choice == 'e':
#         exit()
#     else:
#         print("---- please choose correct choice")
#
#

# typeerror

# res = 4+ 'rrr'


def askforInt(message):
    try:
        num = int(input(message))
    except Exception as e:
        print(e)
        print("---Number is not valid ")
        return False
    else:
        return num
    finally:
        print("----------process completed")
res=askforInt("Enter a number")
print(res)
