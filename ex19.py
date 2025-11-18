def count(a, b):
    if a < b:
        a, b = b, a
    
    if b == 0:
        return 0
    
    sq_count = a // b
    
    ost = count(b, a % b)
    
    return sq_count + ost
    
def main():
    a = int(input())
    b = int(input())
    print(count(a, b))

if __name__ == "__main__":
    main()

