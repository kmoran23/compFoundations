#jes4-3 #KyraMoran

from time import sleep
from random import *

#createWorldAndTurtle
world = makeWorld(300,500)
picTurtle = makeTurtle(world)
penUp(picTurtle)
moveTo(picTurtle,0,0)

#dropBlackBackground
file = pickAFile()
background = makePicture(file)
drop(picTurtle,background)

#drawDynamiteStick
dynamite = makeTurtle(world)
penUp(dynamite)
moveTo(dynamite,150,500)
penDown(dynamite)
dynamite.setPenWidth(20)
dynamite.setPenColor(red)
sleep(.5)
forward(dynamite,40)
penUp(dynamite)
forward(dynamite,5)
sleep(.5)
penDown(dynamite)
dynamite.setPenWidth(3)
dynamite.setPenColor(white)
sleep(.5)
forward(dynamite,15)

#lightTheFuse
sleep(1)
penDown(dynamite)
dynamite.setPenWidth(5)
dynamite.setPenColor(orange)
backward(dynamite,15)
sleep(.5)

#setTurtleAtTopOfFuse
firework = makeTurtle(world)
penUp(firework)
moveTo(firework,150,440)

#defineRandomColorFunction
def randomColor():
   r = randint(0, 255)
   g = randint(0, 255)
   b = randint(0, 255)
   return makeColor(r, g, b)

#fireworks!
for x in range(40): #40fireworks 
  randTurn = randint(-25,25)
  randHeight = randint(150,350)
  firework.setPenColor(randomColor())
  penDown(firework)
  turn(firework,randTurn)
  forward(firework,randHeight)
  turn(firework,-randTurn)
  forward(firework,60)
  backward(firework,30)

  for y in range(5):
    turn(firework,-30)
    forward(firework,30)
    backward(firework,60)
    forward(firework,30)

  penUp(firework)  
  moveTo(firework,150,440)
  turnToFace(firework,150,0)
  sleep(.2)
  
#randomColor function from link below
#http://www.tigerjython.com/engl/index.php?inhalt_links=navigation.inc.php&inhalt_mitte=grafik/zufall.inc.php




  
   

