

def f(l):
	if len(l) == 0:
		return []
	elif len(l) > 0:
		return [l[0], l[0]] + f(l[1:])


print f([1,2,3,4])


def f(l, initial):
	if initial > 0:
		a = l.pop(0)
		l.append(a)
		l.append(a)
		return f(l, initial-1)
	elif initial == 0:
		return []


k=[1,2,3]
f(k, len(k))
print k