#the cons function provided is essentially the same as the lambda expression lambda f :f(a,b)
#print it you function cons.<locals>.pair at some address> 


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(f):
	return f(lambda a, b:a)

	
def car(f):
	return f(lambda a, a:b)


