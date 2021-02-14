
# https://codestepbystep.com/problem/view/python/recursion/move_to_end


def move_to_end(s, ch, count):
	if s:
		if s[0] != ch:
			return s[0] + move_to_end(s[1:], ch, count)
		elif s[0] == ch:
			count[0] += 1
			return move_to_end(s[1:], ch, count) + ch
	else:
		return ""


def moveHelper():
	s = "abacada"
	ch = "a"
	count = [0]
	data =  move_to_end(s,ch, count)
	print("Count is : ", count)
	return data  #+ ch*count[0]

print(moveHelper())
