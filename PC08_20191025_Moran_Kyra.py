#JES 5
#KyraMoran
#created on 10/25/19

import gui
from random import *
from time import sleep


#create super class to make neutral bubbles
class neutral():
  
  #initializer method that gets called when we make a bubble of any type
  def __init__(self,color = gui.Color.DARK_GRAY,diam=40):
    #define some instance properties called diam and color
    self.color = color
    self.diam = diam
    
  #draw method that will work with superclass and subclasses
  def draw(self, panel):
    xpos = randint(60,540)
    ypos = randint(60,540)
    
    #create the bubble
    bubble = gui.Oval(xpos, ypos, xpos + self.diam, ypos + self.diam, self.color, true)
    
    #add an action that will come from superclass or subclass
    bubble = self.addAction(bubble, panel)
    
    panel.add(bubble)
    return bubble #return the object for easy management outside of class
    
  #superclass addAction method that adds a click listener to remove a neutral bubble when it's clicked
  def addAction(self, bubble, panel):
      
    def remove(x,y): #this function removes bubbles from display and list
      disp.remove(bubble) #remove bubble from panel
      objList.remove(bubble) #remove bubble from list
                 
    bubble.onMouseDown(remove) #call remove function when we click the bubble
   
    return bubble
    
  #move bubble function
  def move(self, bubble):
  
    #bubble dances diagonally
    x,y = bubble.getPosition()
    
    #determine how much to move the bubble around
    step = randint(-8,8)
    
    #check to make sure that the new bubble is always inside the bounds of our panel
    if 50 < x + step < 550 and 50 < y + step < 550: #if bubble will stay in bounds
      bubble.setPosition(x + step, y + step) 
      
#friend class    
class friend(neutral):
  #friend specific class attribute that determines how quickly our game moves
  duration = 0.05
   
  #overrides addAction method from the superclass
  def addAction(self, bubble, panel):
    #this function adds an interactive user behavior to an object
      
    def slow(x,y): #this function slows the game down
      disp.remove(bubble) #remove the bubble from the panel
      objList.remove(bubble)
      self.duration += 0.2 #add 0.2 to our duration class attribute   
                  
    bubble.onMouseDown(slow) #add a click listener to remove and slow the game
    
    return bubble

#enemy class    
class enemy(neutral):
  def addAction(self, bubble, panel):
    
    def bubbleDivision(x,y): #this function breaks the enemy bubble into two neutral bubbles
      disp.remove(bubble) #removes enemy bubble from display
      objList.remove(bubble) #removes enemy bubble from list
      for i in range(2): #creates 2 neutral bubbles
        newNeutralBubble = controller.draw(disp)
        objList.append(newNeutralBubble)
        
    bubble.onMouseDown(bubbleDivision)
    
    return bubble
        
#now let's draw our panel and control the behavior
disp = gui.Display('Click Game',600,600)

#create instances for each of our classes
controller = neutral()
friendBubble = friend(color=gui.Color.GREEN, diam = 40)
enemyBubble = enemy(color=gui.Color.RED, diam = 60)

#empty list to store our objects
objList = [] 
  
#start game announcement
start = gui.TextArea ('START GAME', 1, 8)
disp.add(start, 250, 280)
sleep(3)
disp.remove(start)                    

#draw 10 neutral bubbles
for i in range(6):
  newNeutralBubble = controller.draw(disp)
  objList.append(newNeutralBubble)
  
#draw 2 friend bubbles
for i in range(2):
  newFriendBubble = friendBubble.draw(disp)
  objList.append(newFriendBubble) 
  
#draw 2 enemy bubbles
for i in range(2):
  newEnemyBubble = enemyBubble.draw(disp)
  objList.append(newEnemyBubble)

 
#now let's animate by running an infinite while loop
while true:
  if objList == []: #win announcement
    winLabel = gui.TextArea('You win! You popped all the bubbles!', 1, 20)
    disp.add(winLabel, 180, 300)
    break #stop the while loop once all the bubbles have been popped
  for obj in objList:
    controller.move(obj) #call the move method of the controller instance
    
  sleep(friendBubble.duration) #slows the game down by sleeping for the new duration after the friend bubble is clicked
  


  
