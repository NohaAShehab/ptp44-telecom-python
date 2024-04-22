

def askforInt(message="please enter number"):
    while True:
        mynum = input(message)
        if mynum.isdigit():
            mynum = int(mynum)
            return mynum
        print("----- please enter valid number")
