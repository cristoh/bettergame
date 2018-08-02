import random, re, time
from rps import rips

# Edited by ye

#variables
#end variables

#functions
def getDirection():
	choice = raw_input("choose a direction ")
	return choice

def moveLocation(choice):
	if choice == "left" or choicels == "down":
		return -1
	elif choice == "right" or choice == "up":
		return 1
def generateRooms():
	rooms = ["00","10","20","01","11","21","02","12","22"];
	return rooms
def findRoom(rooms,curx,cury):
	roomFound = False
	for room in rooms:
		if curx == int(room[0]) and cury == int(room[1]):
			roomFound = True
	
	return roomFound


#end functions

def game():
	curx = 0
	cury = 0
	rooms = generateRooms()
	roomFound = True
	while True:
		choice = getDirection()
		if choice == "left" or choice == "right":
			curx += moveLocation(choice)
		else:
			if choice == "up" or choice == "down":
				cury += moveLocation(choice)

		roomFound = findRoom(rooms,curx,cury)
		if roomFound:
			print "you are in a room"
		else:
			#C: something like this?
			curx -= moveLocation(choice)
			cury -= moveLocation(choice)
			print "you hit a wall"

		print "x = %s" % str(curx)
		print "y = %s" % str(cury)
rips()
game()

