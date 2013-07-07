import math

def isPrime(p):
	for i in range(2,int(math.sqrt(p))+1):
		if p%i==0:
			return False
	return True

def sum(list):
	sum = 0
	for x in xrange(0,len(list)):
		sum += list[x]
	return sum
		

