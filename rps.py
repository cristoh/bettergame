import random


#functions
def roll(choice):
	won = 0
	compRoll = genRoll()

	if (choice == 1 and compRoll == 3) or (choice == 2 and compRoll == 1) or (choice == 3 and compRoll == 2):
		hasWon = -1
	elif choice == compRoll:
		hasWon = 0
	else:
		hasWon = 1
	return hasWon
def genRoll():
	compRoll = random.randrange(1,4)
	print "The monster rolled a %s " % compRoll 
	return compRoll
#end functions

#varibles

#end variables

def rips():
	options = [1,2,3]
	choice = 0
	hasWon = 0
	myHealth = 100
	hisHealth = 100
	while True:
		choice = int(raw_input("RPS! \n 1 beats 2, 2 beats 3, 3 beats 1 \n>"))
		hasWon = roll(choice)
		if hasWon == 1:
			hisHealth -= 10
			print "u win no health lost. monster has %s health left" % hisHealth
		elif hasWon == -1:
			myHealth -= 10
			print "you have %s health left. monster has %s left" % (myHealth, hisHealth)
		else:
			print "stalemate!"

		if myHealth <= 0:
			print "youre ded"
			return [0, hisHealth]
		elif hisHealth <= 0:
			print "he ded"
			return [myHealth, 0]			
	
