n = 1001
s = [[0 for x in xrange(0,n)] for x in xrange(0,n)]


if __name__ == '__main__':
	cX = cY = n/2
	cY -=1
	# s[cX][cY] = 1
	pointer = 1
	step = 1
	cY += 1
	while step <= n:

		#Right
		for x in xrange(1,step-1):			
			s[cX][cY] = pointer
			print cX,cY,pointer

			cX +=1
			pointer += 1

		#Bottom
		for x in xrange(1,step):
			s[cX][cY] = pointer	
			print cX,cY,pointer

			cY -= 1		
			pointer += 1
		
		#Left
		for x in xrange(1,step):	
			s[cX][cY] = pointer
			print cX,cY,pointer

			cX -= 1
			pointer +=1

		#Top
		for x in xrange(1,step+1):	
			s[cX][cY] = pointer
			print cX,cY,pointer

			cY += 1
			pointer += 1

		step += 2

	sum = 0
	for x in xrange(0,n):
		sum+= s[x][x]+s[n-1-x][x]
		
	print s,product-1