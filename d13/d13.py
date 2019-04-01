def get_all_substrings(s):
	ret = []
	n = len(s)
	for i in range(n):
		for j in range(n - i):
			ret.append(s[j:j + i-1])
	return ret

print(get_all_substrings("abc"))
