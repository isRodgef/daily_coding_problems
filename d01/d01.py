
def d01(lst,k):
	for i in lst:
		if k - i in lst:
			return True
	return False
	
