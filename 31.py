v1 = 1
v2 = 2
v3 = 5
v4 = 10
v5 = 20
v6 = 50
v7 = 100
v8 = 200

n1 = 200/v1+1
n2 = 200/v2+1
n3 = 200/v3+1
n4 = 200/v4+1
n5 = 200/v5+1
n6 = 200/v6+1
n7 = 200/v7+1
n8 = 200/v8+1

def init(waysForN,n):
	for x in xrange(n,201,n):
		waysForN[x] = 1

def combinedWays(ways1, ways2):
	combinedWays = [0 for x in xrange(0,201)]
	for x in xrange(1,201):
		ways = 0
		for y in xrange(0,x+1):
			z = x - y
			ways += ways1[y] * ways2[z]
		ways += ways1[x] + ways2[x]
		combinedWays[x] = ways
	return combinedWays

def combinedWaylist(wayList):
	combinedWaysA = wayList[0]
	for x in xrange(1,len(wayList)):
		combinedWaysA = combinedWays(combinedWaysA, wayList[x])
	return combinedWaysA

if __name__ == '__main__':


	waysFor1 = [0 for x in xrange(0,201)]
	waysFor2 = [0 for x in xrange(0,201)]
	waysFor3 = [0 for x in xrange(0,201)]
	waysFor4 = [0 for x in xrange(0,201)]
	waysFor5 = [0 for x in xrange(0,201)]
	waysFor6 = [0 for x in xrange(0,201)]
	waysFor7 = [0 for x in xrange(0,201)]
	waysFor8 = [0 for x in xrange(0,201)]

	init(waysFor1,1)
	init(waysFor2,2)
	init(waysFor3,5)
	init(waysFor4,10)
	init(waysFor5,20)
	init(waysFor6,50)
	init(waysFor7,100)
	init(waysFor8,200)

	result = combinedWaylist([waysFor1,waysFor2,waysFor3,waysFor4,waysFor5,waysFor6,waysFor7,waysFor8])

	print result[200]