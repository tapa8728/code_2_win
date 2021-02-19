
def f(s, ch1, ch2):
	if len(s) < 1:
		return ""
	elif len(s) >= 1:
		return (ch2 if s[0]==ch1 else s[0]) + f(s[1:], ch1, ch2)


print f("abac", "a", "z")