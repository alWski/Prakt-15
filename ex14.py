def numbers(x):
    if x < 10:
        print(x)
    else:
        print(x % 10)
        numbers(x // 10)
    
def main():
    n = int(input())
    numbers(n)

if __name__ == "__main__":
    main()
