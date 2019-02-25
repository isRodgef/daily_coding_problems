class Tree:
	def __init__(self,value,left=False,right=False)	
		self.values = value
		self.left = left
		self.right = right

	def get_ret(node):
		left_values = get_val(node.left)
		right_values = get_val(node.right)
		count = left_values[0] + rigth_values[0]
		if not node:
			return 0,None
		if left_values and right_values and left_values.values ==right.val and left.val == node.val:
			count+=1 

		return count, node


		

