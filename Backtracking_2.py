# https://www.bilibili.com/video/BV1B4411W7Ld?p=14

'''
Write a recursive function diceroll that accepts an integer representing a number of 6-sided dice to rol and
output all possible combinations of values that could appear on the dice 

diceroll(2)
{1,1}
{1,2}
{1,3} ..... {6,6}

'''

# How is this problem self-similar? 
# it can be solved with a for-loop hence it has smaller solutions


def diceRoll(dice, chosen):
	# base case
	if len(chosen) == dice:
		print chosen

	# recursive case 
	else: 
		 #choose
		 #explore - indicates how many branches each node will fork 
		 diceRoll(dice, chosen + ["1"])
		 diceRoll(dice, chosen + ["2"])
		 diceRoll(dice, chosen + ["3"])
		 diceRoll(dice, chosen + ["4"])
		 diceRoll(dice, chosen + ["5"])
		 diceRoll(dice, chosen + ["6"])

		 #Unchoose

diceRoll(2, [])
