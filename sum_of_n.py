

def f(n):
	if n == 0:
		return 0.0
	elif n==1:
		return 1.0
	else:
		return f(n-1) + float(1)/float(n)


print(f(2))