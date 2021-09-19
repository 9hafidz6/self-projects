# test file for unit testing, simple calculation functions are

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        raise ValueError("cannot divide by 0")
    return a/b
    
def main():
    pass

if __name__ == '__main__':
    main()