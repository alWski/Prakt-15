def ten_to_bin(x):
    if x == 0:
        return "0"
    elif x == 1:
        return "1"
    
    return ten_to_bin(x // 2) + str(x % 2)
    
def main():
    n = int(input())
    print(ten_to_bin(n))

if __name__ == "__main__":
    main()
