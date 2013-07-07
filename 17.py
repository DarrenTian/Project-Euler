count = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',
		7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',
		13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',
		19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',
		80:'eighty',90:'ninety'}

if __name__ == '__main__':
	for x in xrange(21,100):
		if x in count:
			pass
		else:
			r =  x%10
			p = (x-r)/10
			count.setdefault(x,(count[p*10]+count[r]))

	for x in xrange(1,10):
		count.setdefault(x*100,count[x]+'hundred')
		for y in xrange(1,100):
			count.setdefault(x*100+y,count[x*100]+'and'+count[y])
	count.setdefault(1000,'onethousand')

	length = 0
	for x in xrange(1,1001):
		length += len(count[x])
		print x,count[x]

	print length

	