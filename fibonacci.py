a = 0
b = 1
c = a+b

def fibSer(num):
    global a
    global b
    global c
    if num == 0:
        return 
    print(a)
    a = b
    b = c
    c = a + b
    fibSer(num-1)

if __name__ == "__main__":
    fibSer(10)
