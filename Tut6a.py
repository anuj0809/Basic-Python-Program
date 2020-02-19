# map(function to apply, list of inputs)

def square(n):
    return n**2
h1=[1,2,3,4,5,6,7,8,9]
sq = list(map(square,h1))
print(sq)