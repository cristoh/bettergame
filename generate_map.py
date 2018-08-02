from random import randint

class Location:

    def __init__(self, x, y):
        self.x = 0
        self.y = 0

    #def show_all(self):
    #    print(self.X, self.Y)


def drawMap():
  return

def getMap(maxX, maxY, startX, startY, numOfRooms):
  gameMap = []

  curX = startX
  curY = startY
  #generate an x and y
  count = 0

  while count < numOfRooms:
    direction = randint(0,3)
    #check bounds
    if (direction == 0 and curY == 0) or (direction == 1 and curX == maxX) or (direction == 3 and curY == maxY) or (direction == 3 and curX == 0):
      #skip loop iteration, do not increment count
      continue
    
    else:
      if direction == 0:
        curY += 1
      elif direction == 1:
        curX += 1
      elif direction == 2:
        curY -= 1
      elif direction == 3:
        curX -= 1          
      count += 1   
      newRoom = Location(curX, curY)
      gameMap.append(newRoom)  
      print("Room #: " + str(count))
      print("X: " +str(curX))
      print("Y: " + str(curY))

  #returns an array of Location objects which define the rooms of the map
  return gameMap
  #top    - 0
  #right  - 1
  #bottom - 2
  #left   - 3
  

