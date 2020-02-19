# *args and **kwargs tutorial
# *vars and **kvars tutorial

def funtion_1(*args):
    print(type(args))
    if(len(args)==3):
        print("The name of the student is ",args[0], "and age is ",args[1], "and roll no is ",args[2])
    else:
        print("The name of the student is ",args[0], "and age is ",args[1])



lis = ["ABHISHEK",56]
funtion_1(*lis)
