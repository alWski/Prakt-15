def mod_number(a, b):
    if a < b:
        return a
    else:
        return mod_number(a - b, b)

def main():
    a = int(input())
    b = int(input())
    
if __name__ == "__main__":
    main()
