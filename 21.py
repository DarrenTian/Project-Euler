import math
def d(n):
	sum = 0
	for x in xrange(2, int(math.sqrt(n)+1)):
		if n%x==0:
			sum+=x
			if x!=math.sqrt(n):
				sum+=(n/x)
	return sum + 1

if __name__ == '__main__':
	a = {}
	for x in xrange(1,10000):
		pass
		a.setdefault(x,d(x))
	print a
	c = []
	for m in a:
		x = a[m]
		if x in a:
			y = a[x]
			if y==m and m!=x:
				if m not in c:
					c.append(m)

	# c = [m for m in a for n in b m!=n and a[m]==a[n]]
	print c
	sum =0
	for x in c:
		sum += x
	print sum