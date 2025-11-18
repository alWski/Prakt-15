def count(n):
    if n < 10:
        return 1
    else:
        return 1 + count(n // 10)

def main():
    n = int(input())
    print(count(n))

if __name__ == "__main__":
    main()
