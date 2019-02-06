
def d01(lst,k):
	lst = set(lst)
	for i in lst:
		if k - i in lst:
			return True
	return False

if __name__ == '__main__':
	print(d01([1,10,23,24,7],31))	
