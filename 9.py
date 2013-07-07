if __name__ == '__main__':
	sum = 1000
	for a in xrange(1,int(sum/3)+1):
		for b in xrange(a,int(sum/2)+1):
			c= sum -a -b
			# print a,b,c
			if a*a + b*b == c*c:
				print a*b*c,a,b,c