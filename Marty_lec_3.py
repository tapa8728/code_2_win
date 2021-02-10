# https://www.bilibili.com/video/BV1B4411W7Ld?p=10 

'''
Cantor Set 

Try to form a sentence where it describes the problem consisting of itself

Eg: 
A level 7 cantor-set is a line with a level 6 cantorset on the left and a level 6 cantorset on the right 
.... helps us immediately form the tree 

cantorset(x,y,level):
	drawline()
	cantorset(x/3, y, level-1)
	cantorset(2x/3, y, level-1)
	
Implicit base cases are always after optimizing the original code 
'''
