def function1(x):
    if x < 2:
        return 0
    if x == 2:
        return 1
    
    def check_del(n, delit):
        if delit == 1:
            return 1
        if n % delit == 0:
            return 0
        return check_del(n, delit - 1)
    
    return check_del(x, x - 1)
    
def main():
    a = int(input())
    print(function1(a))

if __name__ == "__main__":
    main()
