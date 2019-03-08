def getAllSuffixes(mylist, prefix):
	ret = []
	mylist.sort()
	lst = set(mylist)
	for i in lst:
		if i.startswith(prefix):
			ret.append(i)
	return ret
