#https://www.bilibili.com/video/BV1B4411W7Ld?p=16&spm_id_from=pageDriver

def permuteName(name, chosen, res):
	print "permuteName(",name,",",chosen,")"
	if len(name) == 0:
		#print "inside : ", chosen
		res.append("".join(chosen))
	else:
		# choose

		# explore
		for i in xrange(len(name)):

			permuteName(name[:i]+name[i+1:], chosen + [name[i]], res )

		# unchoose 

res=[]
permuteName(["M","A","R","T","Y"], [], res)
print res