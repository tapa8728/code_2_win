# https://www.bilibili.com/video/BV1B4411W7Ld?p=9

'''
return command is very important 

You want to make sure that all paths of your code (if-else) return a value of some kind. 

PrintBinary 
Base Case - if n in [0,1] then return n itself ( this is easy for a single bit)
Recursive Case -  ??
	what is the easiest way to bite of a chunk ?
	eg:  101101 
	it is easiest to get the last "1" and second-last "0"
 	using div/mod operations. 


Binary of 43 = Binary of 21 (43/2) + Binary of 1 (43%2)

'''

def printBinary(n): # 2
	if n <= 1: # base case 
		print n, # 1
	else: # recursive case 
		prefix = n/2  # 5, 2, 1
		lastdigit = n%2 # 1, 1, 0
		printBinary(prefix) # 5, 2, 1
		print lastdigit, # "1 1 0"

printBinary(3) 

def reverseLines(lines):
	# base case
	if len(lines) == 1:
		print lines[0]
	# recursive case 
	else:
		print lines[-1]
		reverseLines(lines[:-1])

reverseLines(["hello", "line2", "line3", "line4"]) 


# classic recursion implementation
def crawl(path, indent):
	# base case
	if os.path.isfile(path):
		print path 
	# recursive case 
	else: 





import os
absolute_path = os.path.abspath("ebikes.txt")
print("Full path: " + absolute_path)
dir_path = os.path.dirname(absolute_path)
print("Directory Path: " + dir_path) #  /Users/tanvi/Desktop/work_2_win
crawl(dir_path)

