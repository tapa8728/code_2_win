# Sublists 
# https://www.bilibili.com/video/BV1B4411W7Ld?p=17

def sublists(nameList, chosen, res):
	if len(nameList) == 0: # base case 
		res.add(tuple(chosen)) 
	else:
		# choose
		# explore
		sublists(nameList[1:], chosen+[nameList[0]], res) # pick
		# unchoose

		# choose
		# explore
		sublists(nameList[1:], chosen, res)	# dont pick 
		# unchoose

res = set()
sublists(["Tiki", "Mon", "Cow"], [], res)
for each in res:
	print each