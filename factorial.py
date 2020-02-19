def fact(a):
    if a == 0:
        return 1

    return a * fact(a-1)
    

if __name__ == "__main__":
    print(fact(5))
