#https://www.bilibili.com/video/BV1B4411W7Ld?p=16&spm_id_from=pageDriver

def permuteName(name, chosen, res):
	if len(name) == 0:
		res.append("".join(chosen))
	else:
		#choose

		# explore

		# unchoose 

res=[]
permuteName("MARTY", [], res)
print res