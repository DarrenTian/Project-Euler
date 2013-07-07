import math

def getSumOfDivisor(number):
	list = [1]
	for x in xrange(2,int(math.sqrt(number)+1)):
		if number%x == 0 :
			if not x == number/x:
				list.append(x)
				list.append(number/x)
			else:
				list.append(x)
	return sum(list)


if __name__ == '__main__':
	abundant = []
	for x in xrange(1,28124):
		a = getSumOfDivisor(x)
		if a>x:
			abundant.append(x)
	
	sum = 0
	list = [x+y for x in abundant for y in abundant if x+y<28124]
	setList =  set(list)
	# for x in xrange(1,28124):
	# 	for a in abundant:
	# 		if a < x:
	# 			if x-a in abundant:
	# 				sum += x
	# 				print x
	# 				break
	# 		else:
	# 			break
	# print sum
	for x in xrange(1,28124):
		if x not in setList:
			sum+=x
	print sum