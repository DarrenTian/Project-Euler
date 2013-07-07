






def next(n):
	if n%2==0:
		return n/2
	else:
		return n*3+1

if __name__ == '__main__':
	dic = {1:1}
	biggest = 0
	num = 0
	for x in xrange(1,1000000):
		key = x
		count = 0
		while key not in dic:
			key=next(key)
			count = count+1
		count = count + dic[key]
		if count > biggest:
			num = x
			biggest = count
		dic.setdefault(x,count)
		# print dic
		
	print num,biggest


		# count = 0
		# while not x==1:
		# 	x=next(x)
		# 	count +=1
		# if count>biggest:
		# 	biggest = count
		# 	print biggest



# s = 0
# start = 0

# def longest(n):
# 	global s,start


# 	if n==1:
# 		return 0


# 	if (not (n-1)%3==0 ) and (not 2*n<3*1000000+1):
# 		print n,'can not further'
# 		return -1


# 	if ((n-1)%3==0) and (2*n<3*1000000+1):
# 		print n,'can be further in two ways'
# 		a = longest((n-1)/3)+1
# 		b = longest(2*n)+1

# 		# if max(a,b) == 0:
# 		# 	return -1

# 		if a>b:
# 			if a>s:
# 				s=a
# 				start = (n-1)/3
# 		else:
# 			if b>s:
# 				s=b
# 				start = 2*n
# 		# print 3,start,s
# 		print n,'return',max(a,b)
# 		return max(a,b)		

# 	if 2*n<3*1000000+1:
# 		print n,'can be doubled'
# 		a = longest(2*n)+1
# 		# if a==0:
# 		# 	return -1
# 		if a>s:
# 			s=a
# 		start = 2*n
# 		# print 1,start,s
# 		print n,'return',a
# 		return a
# 	if (n-1)%3==0:
# 		print n,'can be divided'
# 		a = longest((n-1)/3)+1
# 		# if a==0:
# 		# 	return -1
# 		if a>s:
# 			s=a
# 		start = (n-1)/3
# 		print n,'return',a
# 		# print 2,start,s

# 		return a
# 	return -1

# if __name__ == '__main__':
# 	# longest(2)
# 	print longest(2),s,start
