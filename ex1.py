def pownum(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a
    else:
        return a * pownum(a, n - 1)

def main():
	a = int(input())
	n = int(input())
	print(pownum(a, n))

if __name__ == "__main__":
    main()
