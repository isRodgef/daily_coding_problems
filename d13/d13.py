def get_all_substrings(s):
	ret = []
	n = len(s)
	for i in range(n):
		for j in range(n - i + 1):
			ret.append(s[j:j + i])
	return ret

def char_count(st):
	return len(set(st))

def len_most_unique_chars(s,n):
	ret_lst = []
	lst = get_all_substrings(s)
	for  i in lst:
		if char_count(i) == n:
			ret_lst.append(i)
	return ret_lst

#print(
subs = get_all_substrings("abc")
f = len_most_unique_chars(subs,2)
a = []
for x in f:
	#if char_count(x) == 2:
	#	a.append(x)
	print(x)
print(a)

