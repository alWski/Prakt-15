def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)

def main():
    a = int(input())
    b = int(input()
    print(count(a, b))

if __name__ == "__main__":
    main()
