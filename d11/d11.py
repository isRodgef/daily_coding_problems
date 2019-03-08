def getAllSuffixes(mylist, prefix):
	ret = []
	mylist.sort()
	lst = set(mylist)
	for i in lst:
		if i.startswith(prefix):
			ret.append(i)

	return ret

if __name__ == '__main__':
	val = ["abc","dab", "a"]
	for  i in range(1000000):
		val.append(chr(i % 128) + "ab")
	print(getAllSuffixes(val,"ab"))
		
	
