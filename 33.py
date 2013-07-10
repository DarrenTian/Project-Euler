import math
def deduct(d2,d1):
	lists = []

	if d2[0]==d1:
		lists.append(d2[1])
	if d2[1]==d1:
		lists.append(d2[0])
	return lists

def step1():
	pairs = [(x,y) for x in xrange(10,100) for y in xrange(10,100)]
	for pair in pairs:
		xStr = str(pair[0])
		yStr = str(pair[1])
		common = set(xStr)&set(yStr)
		if xStr<yStr and common:
			
			for x in common:
				xStrA = deduct(xStr,x)
				yStrA = deduct(yStr,x)
				pairsA = list(set([(x,y) for x in xStrA for y in yStrA if y!='0']))
				if pairsA:
					
					# print float(xStr),float(yStr),float(pairsA[0][0]),float(pairsA[0][1])
					if abs((float(xStr)/float(yStr)-float(pairsA[0][0])/float(pairsA[0][1])))<0.00000001:
						print xStr,yStr,pairsA
					"we find 16,64 19,95 26,65 49,98"

if __name__ == '__main__':
	print "8/800=1/100"
	

		