def search(a, x):
    if not a:
        return 0
    
    if a[0] == x:
        return 1
    
    return search(a[1:], x)
    
def main():
    n = int(input())
    a = [int(input()) for i in range(n)]
    print(search(a))

if __name__ == "__main__":
    main()
