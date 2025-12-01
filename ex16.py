def ten_to_ran(x, n):
    if n // x == 0:
        return str(n%x)
    if n % x > 9:
    	s = 'ABCDEF'
    	return ten_to_ran(x, n // x) + str(s[(n % x) % 10])
    return ten_to_ran(x, n // x) + str(n % x)
    
def main():
	x = int(input())
	n = int(input())
	print(ten_to_ran(x, n))

if __name__ == "__main__":
    main()
