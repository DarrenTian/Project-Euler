import math
def getN():
	n=1
	while n*math.factorial(9)>math.pow(10,n)-1:
		n += 1
	return n

if __name__ == '__main__':
	dic ={}
	for x in xrange(0,10):
		dic.setdefault(x,math.factorial(x))
	n = getN()

	for x in xrange(3,int(math.pow(10,n))-1):
		if x==sum([dic[int(num)]for num in str(x)]):
			print x	
		