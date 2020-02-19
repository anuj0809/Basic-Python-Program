def funtion_1(*args):
    print(type(args))
    if(len(args)==3):
        print("The name of the student is ",args[0], "and age is ",args[1], "and roll no is ",args[2])
    else:
        print("The name of the student is ",args[0], "and age is ",args[1])



def print_marks(**kwargs):
    print(type(kwargs))
    for name,marks in kwargs.items():
        print(name,marks)

def master(normal, *args, **kwargs):
    print(normal)
    for i in args:
        print(i, " ",end="")
    print()
    for name, marks in kwargs.items():
        print(name, marks)



lis = ["abhishek",17,43435]
marklist = {"ABHISHEK" :100,"MAZHARAIN" :99,"AKSHDEEP" : 32,"AKSHAT" :78}
# print_marks(**marklist)

master("normal_arg", *lis, **marklist)