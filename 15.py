dic = {(20,20):0}

def getPath(sx,sy,e):
	global dic
	if (sx,sy) in dic:
		return dic[(sx,sy)]

	if sx == e:
		return 1
	if sy == e:
		return 1

	path = getPath(sx+1,sy,e) + getPath(sx,sy+1,e)
	dic.setdefault((sx,sy),path)
	return path

	

if __name__ == '__main__':
	for x in xrange(20,-1,-1):
		for y in xrange(20,-1,-1):
			getPath(x,y,20)
	print dic[(0,0)]
		