from string import ascii_lowercase as lower


def two_perm(num):
	ret = []
	ret.append((lower[int(num[0]) - 1],lower[int(num[1]) - 1]))
	numerical = int(num)
	if numerical < 26:
		ret.append(lower[numerical - 1])
	return ret



def loop(numstr):
	i = 0
	full_lst = []
	size = 2
	while i < len(numstr) - 1:
		print(numstr[i:i+2])
		full_lst.append(two_perm(numstr[i:i+2]))
		i+=1
		size+=1 
	return full_lst	
	

print(loop("1111"))
