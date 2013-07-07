def fact(n):
	if n==1:
		return 1
	else:
		return n*fact(n-1)

if __name__ == '__main__':
	x = fact(100)
	s = str(x)
	sum = 0
	for t in s:
		sum += int(t)
	print sum