low = 2
high = 100
distinct = []

if __name__ == '__main__':
	for x in xrange(low,high+1):
		product = x
		for y in xrange(low,high+1):
			product = product * x
			if product in distinct:
				pass
			else:
				distinct.append(product)

	print len(distinct)

