

# def f(s):
# 	if len(s) <= 1:
# 		return True
# 	elif len(s) > 1: 
# 		return (True if s[0]<=s[1] else False) and f(s[1:])


# print f("0121")
# print f("1111")


def f(s, c):
	if len(s) <=1:
		return s
	elif s[0] != c:  #a 
		return s[0] + f(s[1:], c)
	elif len(s) > 1 and s[0] != s[1]:
		return c + f(s[1:], c)
	elif len(s) > 1 and s[0] == s[1]:
		return "" + f(s[1:], c)


print f("abaaaaaaa", "a")