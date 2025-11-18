def progress(a1,r,n):
	if n == 1:
		return a1
	else:
		return progress((a1+r), r, n-1)

def main():
        a1 = int(input())
        r = int(input())
        n = int(input())
        print(progress(a1, r, n))


if __name__ == "__main__":
    main()
