'''

Iterable -
Iterator -
Iteration -

'''
def generator(n):
    for i in range(n):
        yield i

ob1 = generator(266)
print(next(ob1))
print(next(ob1))
print(next(ob1))
print(next(ob1))
print(next(ob1))
print(next(ob1))
print(next(ob1))