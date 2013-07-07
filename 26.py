def getDigits(n):
	digits = []
	remains = []
	remain = 1
	while not remain == 0:		
		while remain<n:
			remain = remain * 10
		p= remain/n
		r= remain%n
		
		
		print p,r
		if r in remains:
			break
		remain = r
		remains.append(r)
		digits.append(p)
	return digits

if __name__ == '__main__':
	map = {}
	for x in xrange(1,1000):
		map.setdefault(len(getDigits(x)),x)
	print map[max(map.keys())]

