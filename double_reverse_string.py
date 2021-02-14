
# f(abc) = ccbbaa 

def f(s):
	if len(s) > 0:
		return s[-1]*2 + f(s[:-1]) 
	else:
		return ""


print f("abcd")