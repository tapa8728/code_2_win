


def f(k):
	return '#' if k==0 else f(k-1)*2 

print f(3)