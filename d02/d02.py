from copy import copy

def mul(arr):
	cp = arr 
	ret = []
	product = 1
	i = 0 
	while i < len(arr):
		product = 1
		cp = copy(arr)
		del cp[i]
		for  j in cp:
			product *= j

		ret.append(product)
		i += 1
	
	return ret

if __name__ == '__main__':
	print (mul([1,2,3,4]))
