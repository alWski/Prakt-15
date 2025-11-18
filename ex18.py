def simmetr(s, i, j):
    if i >= j:
        return True
    
    if s[i] == s[j]:
        return simmetr(s, i + 1, j - 1)
    else:
        return False
    
def main():
    s = "sefjsjeffffdddad"
    i = int(input())
    j = int(input())
    print(simmetr(s, i, j))

if __name__ == "__main__":
    main()
