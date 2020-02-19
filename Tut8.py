import bisect
h1 = [1,2,3,4,6,7,9,43,543,6366]
num = int(input("ENTER A NUMBER"))
print(bisect.bisect(h1,num))
bisect.insort(h1,num)
print(h1)

# MAKE YOUR OWN FUNCTION TO ACCOMPLISH THE SAME TASK
'''
h1 = [1,2,3,4,5,6,7,8,9]
print(h1[::-1])
'''
