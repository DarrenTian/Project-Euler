import math

def getP(r):
	x=[]
	for i in xrange(2,r+1):
		if isPrime(i):
			x.append(i)
	return x

def getNP(r):
	x=[]
	for i in xrange(2,r+1):
		if not isPrime(i):
			x.append(i)
	return x

def isPrime(p):
	for i in range(2,int(math.sqrt(p))+1):
		if p%i==0:
			return False
	return True


def divide(x,y):
	if x<y:
		for i in xrange(x,0,-1):
			if x%i==0 and y%i==0:
				return i
	else:
		for i in xrange(y,0,-1):
			if x%i==0 and y%i==0:
				return i


def multiple(x):
	if len(x)==1:
		return x[0]
	else:
		m=multiple(x[1:])
		d=divide(x[0],m)
	return m*x[0]/d

if __name__ == '__main__':
	x = multiple(range(1,21))
	print x

	# r=10
	# x=r
	# divisible = False
	# while not divisible:		
	# 	x = x+r
	# 	divisible = True
	# 	for i in xrange(1,r):
	# 		divisible = divisible and x%i==0
	# 		print x

	