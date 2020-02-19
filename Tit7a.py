'''
Syntax:
lambda argument : manipulate(argument)
'''

# def add(a, b):
#     s = a+b
#     return s
add = lambda x, y: x + y
print(add(4, 12))

# def x(val):
#     return val[1]

a = [(1, 2), (4, 5), (555, 34)]
a.sort(key=lambda x: x[1])

print(a)