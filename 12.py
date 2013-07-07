import math

def getDivisors(t):
	count = 0
	for x in xrange(1,int(math.sqrt(t)+1)):
		if t%x==0:
			count +=2
	if math.sqrt(t) == int(math.sqrt(t)):
		count -=1
	return count






if __name__ == '__main__':
	t = 1
	count =1
	while getDivisors(t)<=500:
		count +=1
		t = t+count
		print t