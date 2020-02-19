'''

List Comprehensions
Dictionary Comprehensions
Set Comprehensions
Generator Comprehensions

'''


list_1 = [1,3,4,6,43,4,6353,6,6,3,6,34,5,23,432,5,42,65,32,5,34,5,43,452,32]
divide_by_3 = []
for item in list_1:
    if item%3 == 0:
        divide_by_3.append(item)
print("BY TRADITIONALL METHOD", divide_by_3)
print("USING LIST COMPREHENTIONS", [item for item in list_1 if item%3==0])

dict1 = {'a':45, 'b':65, 'A':5}
print({k.lower():dict1.get(k.lower(), 0)+dict1.get(k.upper(), 0) for k in dict1.keys()})

sq = {x**2 for x in [1,2,2,1,3,3,4,4,5,5]}
print(sq)