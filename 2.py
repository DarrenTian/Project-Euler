if __name__ == '__main__':
	

	fn1=1
	fn2=2
	fn3=3
	sum = 2

	while(fn3<=4000000):
		fn1=fn2
		fn2=fn3
		fn3=fn1+fn2
		if fn3%2==0:
			sum+=fn3
	print sum