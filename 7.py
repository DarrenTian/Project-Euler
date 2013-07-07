import math
def isPrime(x):
	for i in xrange(2,int(math.sqrt(x))+1):
		if x%i==0:
			return False
	return True


if __name__ == '__main__':
	p = 2
	count =1
	while count <10001:
		p = p+1
		if isPrime(p):
			count = count+1
	print p