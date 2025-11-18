def ind_max(a, index=0, max_index=0):
    if index == len(a):
        return max_index
    
    if a[index] > a[max_index]:
        max_index = index
    
    return ind_max(a, index + 1, max_index)
    
def main():
    n = int(input())
    a = [int(input()) for i in range(n)]
    print(ind_max(a))

if __name__ == "__main__":
    main()
