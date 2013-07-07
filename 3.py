import math

v = 600851475143

def isPrime(p):
	for i in range(2,int(math.sqrt(p))+1):
		if p%i==0:
			return False
	return True
		
def nextPrime(p):
	while(p<=v):
		p += 1
		if(isPrime(p)):
			return p
	return p

if __name__ == '__main__':
	x=0
	p=1
	while v!=1:
		p=nextPrime(p)
		print p
		while v%p==0:
			v=v/p
			x=p
	print x
