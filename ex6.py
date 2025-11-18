def degree5(n):
    if n == 1:
        return 0
    
    if n < 1 or n % 5 != 0:
        return -1
    
    result = degree5(n // 5)
    
    if result == -1:
        return -1
    else:
        return result + 1

def main():
    n = int(input())
    print(degree5(n))

if __name__ == "__main__":
    main()
