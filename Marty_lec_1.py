
# https://www.bilibili.com/video/BV1B4411W7Ld?p=8 

'''
When you think about recursion, think about a bunch of small workers solving a larger problem

Eg - Find the total number of students in a column.
In this case, the workers are each of the students themselves. 
No for loops as we dont want one worker to do all the work, instead we want each worker to do its own 
work and help towards the final solution

No one worker is doing all of the work. 
Each worker is following the same instructions. 


Every recursive algorithm involves 2 parts with an if-else 

1) BASE CASE -  no complications, just one condition. 
>> It is a simple problem that a the function can solve right away. 

2) RECURSIVE CASE -  
How is this problem similar to itself? 
How is this problem similar to smaller
copies of the same problem?  
>> A more complex occurrence of the problme that cannot be directly
answered, but can instead be described in terms of smaller occurrences of the same problem. 


Key Idea - In a recursive piece of code, you handle a small part of the overall task yourself, then 
make a recursive call to handle the rest 



'''

def printStars(n):
	# base case : when should you stop printing? When n=0 
	if n == 0:
		return
	# recursive case : print one star at a time
	else:
		print "*"
		printStars(n-1)

printStars(5)