import myMath

maxN = 0
maxA = 0
maxB = 0

a = 0
b = 0

range = 999

def qSum(n,a,b):
	return n*n+a*n+b


if __name__ == '__main__':
	for a in xrange(-range,range):
		for b in xrange(-range,range):
			n = 0
			sum = qSum(n,a,b)
			while (sum>0) and (myMath.isPrime(sum)):
				if n > maxN:
					maxN = n
					maxA = a
					maxB = b
				n += 1
				sum = qSum(n,a,b)
				print a,b,n,sum
				

	print maxN, maxA, maxB, maxA*maxB
	