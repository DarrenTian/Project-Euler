import re

f = open('triangle.txt')
group = []

if __name__ == '__main__':
	try:
		for line in f:
			t =  re.findall('[0-9][0-9]',line)
			group.append(t)
	finally:
		f.close()

	for x in xrange(1,len(group)):
		for y in xrange(0,len(group[x])):
			if y==0:
				group[x][y] =  str(int(group[x][y])+int(group[x-1][y]))
				print group[x][y],1
			elif y==(len(group[x])-1) :
				group[x][y] =  str(int(group[x][y])+int(group[x-1][y-1]))
				print group[x][y],2

			else:
				group[x][y] = str(max(int(group[x][y])+int(group[x-1][y]),int(group[x][y])+int(group[x-1][y-1])))
				print group[x][y],3

		print group[x]

	l = [int(x) for x in group[len(group)-1]]
	print max(l)
	# print f
	# try:
	# 	for line in f:
	# 		print line
	# finally:
	# 	f.close()
