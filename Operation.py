# sum of two numbers
def sum(a, b):
    print(a+b)

# difference of two numbers
def diff(a, b):
    print(a-b)

# multiplication of two numbers
def mul(a, b):
    print(a*b)

# devision of two numbers
def div(a, b):
    print(a/b)


if __name__ == "__main__":
    # taking input from user and storing in a
    a = int(input("Enter first number\n"))    
    # taking input from user and storing in b
    b = int(input("Enter second number\n"))   
    # sum will calculate the sum of a and b
    sum(a,b)
    diff(a, b)
    mul(a, b)
    div(a, b)