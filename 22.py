import re
f = open('names.txt')
a = []
alpha = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

# def compare(a,b):
# 	if a<b:
# 		return -1
# 	if
	# print 'here'
	# a = a.replace('\"','')
	# b = b.replace('\"','')
	# # print 'compare',a,b
	# # print a,b
	# for x in xrange(0,min(len(a),len(b))):
	# 	if alpha[a[x]] == alpha[b[x]]:
	# 		continue
	# 	else:
	# 		return alpha[a[x]] - alpha[b[x]]
	# if len(b)>len(a):
	# 	return -1
	# elif len(b)<len(a):
	# 	return 1
	# else:
	# 	return 0

def value(x):
	sum = 0
	x = x.replace('\"','')
	for t in x:
		sum += alpha[t]
	return sum
	

def findMin(a):
	# print a
	
	s = a[0]
	for x in a:
		if x < s:
			s = x

		# if compare(x,s)<0:
		# 	s = x
	a.remove(s)
	return s



if __name__ == '__main__':
	try:
		for line in f:
			a =  re.findall('\".*?\"',line)
	finally:
		f.close()
	print a
	s = []
	# print a
	sum = 0

	while len(a)>0:
		x = findMin(a)
		while x in a:
			a.remove(x)
		# print x,'\n'
		s.append(x)
		print x,len(s),value(x)
		# if x=='COLIN':
		# 	print len(s)

	# print s.index('COLIN')
		sum += len(s)*value(x)
	print sum
	# print s

