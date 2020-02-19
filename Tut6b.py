def greater_than_2(n):
    if n > 2:
        return True
    else:
        return False
h1 = [1,2,3,4,5,2,4,56,7,0,0,-2,7,-54,7,98]
greater_2_lst=list(filter(greater_than_2,h1))
print(greater_2_lst)
