#JES4-3 #KyraMoran #created 9/20/19

#this program makes shapes based on the x and y coordinate range in the picture

from random import *

#makeBackground
lightBlue = makeColor (100,150,200)
pic = makeEmptyPicture(600,600,lightBlue)


pink1 = makeColor (230, 160, 160) #just wanted to practice making a color
  
for i in range (200):
  xCord = randint(0,600) #starting x coordinate
  yCord = randint(0,600) #starting y coordinate
  circle = randint(10,60) #height and width of circles
  square = randint(10,100) #height and width of squares
  ovalWidth = randint (10,50) #width of ovals
  ovalHeight = randint (10,80) #height of ovals
  
  if xCord < 200: #left third
    addOval(pic,xCord,yCord, circle, circle, green)
    
  elif 200 < xCord < 400: #middle third
    if yCord < 200:
      addRect(pic, xCord, yCord, square, square, pink1) #top third
    elif 200 <= yCord <= 400:
      addRect(pic, xCord, yCord, square, square, blue) #middle third   
    else:
      addRect(pic, xCord, yCord, square, square, yellow) #bottom third
    
  else: #right third
    addOval(pic, xCord, yCord, ovalWidth, ovalHeight, lightGray)

show(pic)


  
    
    
