def fibSer(num, a, b):

    if num == 0:
        return 
    
    print(a)
    fibSer(num-1, b, a+b)   # Recursion

if __name__ == "__main__":
    fibSer(10, 0, 1)
