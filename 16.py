if __name__ == '__main__':
	s = ['1']
	
	for x in xrange(0,1000):
		extra = 0
		for y in xrange(0,len(s)):
			t = int(s[y])*2+extra
			if t>=10:
				extra = 1
			else:
				extra = 0
			s[y] = str(t%10)
			
		if extra == 1:
			s.append(str(extra))
		print s
	sum = 0
	# print s
	for x in xrange(0,len(s)):
		sum += int(s[x])
	print sum
		
			


			