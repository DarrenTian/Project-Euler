import math
def isPrime(p):
	for x in xrange(2,int(math.sqrt(p)+1)):
		if p%x==0:
			return False
	return True

if __name__ == '__main__':
	sum = 0
	for x in xrange(2,2000000):
		if isPrime(x):
			print x
			sum += x
	print sum