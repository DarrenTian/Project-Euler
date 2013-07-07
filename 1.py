if __name__ == '__main__':
	sum = 0;
	for x in xrange(1,1000):
		if (x%3==0) |(x%5==0):
			sum=sum+x
	print sum