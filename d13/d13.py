def get_all_substrings(s):
	ret = []
	n = len(s)
	for i in range(n):
		for j in range(n - i + 1):
			ret.append(s[j:j + i])
	return ret

print(get_all_substrings("abc"))
