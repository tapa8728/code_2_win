# https://www.bilibili.com/video/BV1B4411W7Ld?p=13 


'''

PrintBinary - 
look for self-similarity 

printbinary(2) amswers need to be used to build printbinary(3) 
OR 

in order to get an answer for printbinary(3) -- we need to get an answer for printbinary(2) and 
for printbinary(2) we need printbinary(1) .... 

hence what is the single-final step that contains all the default answers?
printbinary(1) -- BASE CASE 
0
1 

Prefix string represents a set of choices made by me so far.
Its a time capsule by my ancestors

Hence the base case is when we have gotten  the digits value to 0.
Chip away at the digits --- drive it to the base case 



'''

def printBinary(digits):
	prefix = ""
	_printBinary(digits, prefix)

def _printBinary(digits, prefix):
	# base case 
	if digits == 0 :
		print prefix
	else: #recursive case
		# choose 0
		prefix_0 = prefix + "0"
		digits = digits-1 
		# explore 0
		_printBinary(digits, prefix_0)
		# unchoose 0
		prefix_0 = prefix
		digits = digits+1

		# choose 1
		prefix_1 = prefix + "1"
		digits = digits-1 
		# explore 1
		_printBinary(digits, prefix + "1")
		#unchoose 1
		prefix_1 = prefix
		digits = digits+1 
		

printBinary(3)