
def f(n):
	if n <=1:
		return str(n)
	elif n > 1:
		return f(n//2) + ("1" if n%2!=0 else "0") 

print f(2)
print f(3)
print f(4)