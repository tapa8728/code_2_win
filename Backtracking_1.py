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
	#_printBinary(digits, prefix)
	_pBinary(digits, prefix, "") #indent added 

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
	

# succint version
def _pBinary(digits, prefix, indent):
	print indent, "_pBinary(", digits, ",", prefix, ")"
	if digits == 0:
		print indent, prefix
	else:
		# choose 
		# explore
		_pBinary(digits-1, prefix + "0", indent + "	") # local function variables take care of the choosing/unchoosing
		_pBinary(digits-1, prefix + "1", indent + "	")
		# unchoose 

printBinary(3)

'''
_pBinary( 3 ,  )
	_pBinary( 2 , 0 )
		_pBinary( 1 , 00 )
			_pBinary( 0 , 000 )
			000
			_pBinary( 0 , 001 )
			001
		_pBinary( 1 , 01 )
			_pBinary( 0 , 010 )
			010
			_pBinary( 0 , 011 )
			011
	_pBinary( 2 , 1 )
		_pBinary( 1 , 10 )
			_pBinary( 0 , 100 )
			100
			_pBinary( 0 , 101 )
			101
		_pBinary( 1 , 11 )
			_pBinary( 0 , 110 )
			110
			_pBinary( 0 , 111 )
			111
'''

print "-----------------"

'''
Write a recursive function printDecimal that accepts an integer number of digits and prints all 
base-10 numbers that have exactly that many digits, in ascending order, one per line.


There are many calls here to be made at a single level. Each call is going to handle a decision to be made. 
Hence, we can use a For-loop to make those calls. We are NOT using a for-loop to solve the actual 
problem. That will be done by recursion 
'''

def printDecimal(digits, prefix):
	# base case
	if digits == 0: 
		print prefix + ", ",
	else:  # recursive case 
		#choose
		#explore 
		printDecimal(digits-1, prefix + "0")
		printDecimal(digits-1, prefix + "1")
		printDecimal(digits-1, prefix + "2")
		printDecimal(digits-1, prefix + "3")
		printDecimal(digits-1, prefix + "4")
		printDecimal(digits-1, prefix + "5")
		printDecimal(digits-1, prefix + "6")
		printDecimal(digits-1, prefix + "7")
		printDecimal(digits-1, prefix + "8")
		printDecimal(digits-1, prefix + "9")
		#unchoose 

printDecimal(2, "")