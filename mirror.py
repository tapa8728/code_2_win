
def f(n):
	if n <=0:
		return ""
	elif n == 1:
		return "1"
	elif n%2 == 0: #even 
		return str(n//2) + f(n-2) + str(n//2)
	elif n%2 != 0: #odd 
		return  str(n//2 + 1) + f(n-2) + str(n//2 + 1) 
	

print f(1)
print f(2)
print f(3)
print f(4)
print f(5)
print f(6)
print f(7)
print f(8)