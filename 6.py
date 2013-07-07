def sumOfSquare(r):
	result = 0
	for x in xrange(1,r+1):
		result += x*x

	return result

def  squareOfSum(r):
	result = 0
	for x in xrange(1,r+1):
		result +=x

	return result * result

if __name__ == '__main__':
	r = 100
	x = sumOfSquare(r)
	y = squareOfSum(r)
	print y -x