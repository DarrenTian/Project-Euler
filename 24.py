def getPermutation(digits):
	if digits == []:
		return [''] 
	permutations = []
	for x in digits:
		temp = list(digits)
		temp.remove(x)
		# print temp
		rePerm = getPermutation(temp)
		# permutations = permutations + [x+y for y in rePerm]
		# print rePerm
		# for p in rePerm:
		# 	print permutations.append(x)
		for p in rePerm:
			permutations.append(str(x)+p)

	return permutations

if __name__ == '__main__':
	p = getPermutation([0,1,2,3,4,5,6,7,8,9])
	print p[999999]

		