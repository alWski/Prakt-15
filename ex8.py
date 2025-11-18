def fib(k):
    if k == 1:
        return 0  
    elif k == 2:
        return 1  
    else:
        return fib(k - 1) + fib(k - 2)  

def main():
    n = int(input())
    print(fib(n))

if __name__ == "__main__":
    main()
