import math
7
def isPanDigital(x,y,z):
	lists = list(str(x)+str(y)+str(z))
	lists.sort()
	return lists == ['1','2','3','4','5','6','7','8','9']

if __name__ == '__main__':
	products = []
	lists =  []
	for x in xrange(1,10):
		for y in xrange(x,10):
			z = 9 - x - y
			if (math.pow(10,x-1)*math.pow(10,y-1)<math.pow(10,z+1)-1) and ((math.pow(10,x)-1)*(math.pow(10,y)-1)>math.pow(10,z)-1):
				lists.append([x,y,z])

	for l in lists:
		# print x
		mCandN = l[0]
		mErN = l[1]
		for y in xrange(int(math.pow(10,mCandN-1)),int(math.pow(10,mCandN)-1)):
			for z in xrange(int(math.pow(10,mErN-1)),int(math.pow(10,mErN)-1)):
				product = y*z
				if isPanDigital(y,z,product) and product not in products:
					products.append(product)
	print sum(products)
