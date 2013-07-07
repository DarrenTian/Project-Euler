if __name__ == '__main__':
	count = 2
	digit = 1
	f1 = 1
	f2 = 1
	while digit<1000:
		count +=1
		f3 = f1+f2
		f1=f2
		f2=f3
		digit = len(str(f3))
	print count