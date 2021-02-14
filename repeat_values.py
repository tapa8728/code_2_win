


def f(ch, n, d):
	if n <= 0: 
		return ""
	elif n > 0 and n%2 == 0: # even
		if (ch, n//2) not in d:
			data = f(ch, n//2, d) 
			d[(ch, n//2)] = data 
			return data + data
		else:
			return d[(ch, n//2)] + d[(ch, n//2)]
	elif n > 0 and n%2 !=0: # odd
		if (ch, n//2) not in d:
			data = f(ch, n//2, d)
			d[(ch, n//2)] = data 
			return data + ch + data
		else:
			return d[(ch, n//2)] + ch + d[(ch, n//2)]

print f("bz", 3, {})