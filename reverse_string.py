

def f(s, b, e):
	if b <= e:
		s[b], s[e] = s[e], s[b]
		f(s, b+1, e-1)
	else:
		return None 

s = list("abcde")
print(s)
f(s, 0, len(s)-1)
print(s)