import math
import myMath

if __name__ == '__main__':
	n = 1
	left = math.pow(10,n)
	right = n*math.pow(9,5)
	numbers = []

	while left<right:
		n += 1
		left = math.pow(10,n)
		right = n*math.pow(9,5)
	
	for x in xrange(2,int(left)):
		xStr = str(x)
		sum = 0
		for y in xrange(0,len(xStr)):
			sum += math.pow(int(xStr[y]),5)

		if x == sum:
			numbers.append(x)
	
	print numbers, myMath.sum(numbers)