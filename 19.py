def isLeap(year):
	return (year%4==0) and year%400 !=0

def getDays(year,month):
	if (month==1) or (month==3)or (month==5)or (month==7)or (month==8)or (month==10)or (month==12):
		return 31
	if (month==4)or (month==6)or (month==9)or (month==11):
		return 30
	if month == 2:
		if isLeap(year):
			return 29
		else:
			return 28

def getNextDate(s):
	s[2] +=1
	if s[2]>getDays(s[0],s[1]):
		s[2] = 1
		s[1] += 1
		if s[1]>12:
			s[1] = 1
			s[0] += 1
	return s



def getWeekDay(s,e,weekday):
	while s!=e:
		s= getNextDate(s)
		if weekday==7:
			weekday = 1
		else:
			weekday +=1
	return weekday

def getSum(s,e,weekday):
	sum = 0
	while s!=e:
		s= getNextDate(s)
		if weekday==7:
			weekday = 1
			if s[2]==1:
				sum +=1
		else:
			weekday +=1
	return sum
		


if __name__ == '__main__':
	date = [1900,1,1]
	weekday = getWeekDay(date,[1901,1,1],1)
	sum = getSum([1901,1,1],[2000,12,31],weekday)
	print sum
