import gui
from random import *
import timer
from time import sleep

#created by Kyra Moran and Patricia Chin
#created on 10/04/19
#JES 5
#This program creates a petri dish with animated microbes.

#create panel and petri dish
disp = gui.Display("petri dish", 500, 500,0,0, gui.Color.GRAY)
circle2 = gui.Oval(25,25,475,475, gui.Color.WHITE, true)
disp.add(circle2)
circle = gui.Oval (40, 40, 460, 460, gui.Color(210,180,140), true)
disp.add(circle)

#define random color function
def randColor():
  r = randint(0,255)
  g = randint (0,255)
  b = randint (0,255)
  color = gui.Color(r,g,b) 
  return color 
  
#create empty list to be appended later
MicrobeList= []

#make lines #horizontal
def makeMicrobe(x, y, color, shape):
  if shape == 'hex': 
    hex = gui.Polygon([x, x+10, x+20, x+10, x, x-10], [y, y, y+10, y+20, y+20, y+10], color, true)
    disp.add(hex)
    MicrobeList.append(hex)
    
  elif shape == 'horizLine':
    line = gui.Line(x, y, x+30, y, color, 5)
    disp.add(line)
    MicrobeList.append(line)
    
  elif shape == 'slantLine':
    line2 = gui.Line(x, y, x+40, y+10, color, 5)
    disp.add(line2)
    MicrobeList.append(line2)
  
#make hexagons   
for z in range(20):  
 x = randint (90, 390) 
 y = randint (90, 390)
 makeMicrobe(x,y,randColor(), 'hex')
  
#make horizontal lines
for i in range (20):
  x = randint (90, 390)
  y = randint (90, 390)
  makeMicrobe(x, y, gui.Color.GRAY, 'horizLine')
  
#make slanted lines
for j in range (20):
  x = randint (90, 390)
  y = randint (90, 390)
  makeMicrobe(x, y, gui.Color.WHITE, 'slantLine') 
  
#animation
def micAnimation():
 for microbe in MicrobeList:
   x,y = microbe.getPosition()
   microbe.setPosition(x+10,y)
   sleep(.1)    
   microbe.setPosition(x,y)  
   
#this is supposed to run forever we know this is not ideal lol   
while true:
  micAnimation()
  
printNow ("dancing Gushers!")

  
