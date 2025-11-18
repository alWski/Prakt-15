def combin(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return combin(n, k - 1) * (n - k + 1) // k
def main():
    n = int(input())
    k = int(input())
    print(combin(n, k))

if __name__ == "__main__":
    main()
