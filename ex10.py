def maxlist(a):
    if len(a) == 0:
        return None
    
    if len(a) == 1:
        return a[0]
    
    first_elem = a[0]
    
    res_list = a[1:]
    max_other = maxlist(res_list)

    if first_elem > max_other:
        return first_elem
    else:
        return max_other

def main():
    n = int(input())
    a = [input() for i in range(n)]
    print(maxlist(a))

if __name__ == "__main__":
    main()
