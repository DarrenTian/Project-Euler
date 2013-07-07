def isPalindromic(z):
	s = str(z)
	for x in xrange(0,int((len(s)+1)/2)):
		if s[x] != s[len(s)-1-x]:
			return False
	return True

if __name__ == '__main__':
	big = 0
	for x in xrange(999,99,-1):

		for y in xrange(999,99,-1):
			z = x*y
			if(isPalindromic(z)):
				if z>big:
					big=z
	print big
					