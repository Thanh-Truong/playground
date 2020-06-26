def fibonaci0(n):
    if (n == 0):
        return 0
    elif n == 1:
        return 1
    else:
        return fibonaci0(n - 1) + fibonaci0(n - 2)

def fib(n, a = 0, b = 1):
    print("n={}.a={}.b={}".format(n, a, b)) 
    if n == 0: 
        return a 
    if n == 1: 
        return b 
    return fib(n - 1, b, a + b)

def main():
    print(fib(0))
    print(fib(1))
    print(fib(2))
    print(fib(3))
    print(fib(4))
    print(fib(5))
    #print(fib(9))
if __name__ == "__main__":
    main()