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
	x = 0
	while x<201:
		print x
		waysForN[x]=1
		x+=n

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




	# for x8 in xrange(0,n8):
	# 	for x7 in xrange(0,n7):
	# 		for x6 in xrange(0,n6):
	# 			for x5 in xrange(0,n5):
	# 				for x4 in xrange(0,n4):
	# 					for x3 in xrange(0,n3):
	# 						for x2 in xrange(0,n2):
	# 							for x1 in xrange(0,n1):
	# 								pi = x1*v1+x2*v2+x3*v3+x4*v4+x5*v5+x6*v6+x7*v7+x8*v8

	# 								if pi == 200:
	# 									print pi
	# 									way =[x1,x2,x3,x4,x5,x6,x7,x8]
	# 									print way
	# 									ways.append(way)

	print waysFor1,waysFor2