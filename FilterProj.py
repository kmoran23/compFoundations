#JES 5
#Kyra Moran and Patricia Chin
#created on 12/06/19

import gui

#draw gui panel
disp = gui.Display('Filter GUI', 200, 630)

#just setting values so we can make these variables global
orig = 1
image = 1

#select image callback function
def selectImage():
  global orig, image
  file = pickAFile() #image must be relatively small
  image = makePicture(file) #making two copies so that we can reset image later
  orig = makePicture(file) #making two copies so that we can reset image later
  show(image)

#red tint
def Red(image):
  for p in getPixels(image):
    newRed = getRed(p) * 1.1
    newGreen = getGreen(p) * 0.2
    newBlue = getBlue(p) * 0.2
    setColor(p, makeColor(newRed, newGreen, newBlue))
  repaint(image)
  
#orange tint
def Orange(image):
  for p in getPixels(image):
    newRed = getRed(p) * 1.4
    newGreen = getGreen(p) * 0.8
    newBlue = getBlue(p) * 0.1
    setColor(p, makeColor(newRed, newGreen, newBlue))
  repaint(image)
  
#yellow tint
def Yellow(image):
  for p in getPixels(image):
    newRed = getRed(p) * 1.2
    newGreen = getGreen(p) * 1.1
    newBlue = getBlue(p) * 0.1
    setColor(p, makeColor(newRed, newGreen, newBlue))
  repaint(image)
    
#green tint
def Green(image):
  for p in getPixels(image):
    newRed = getRed(p) * 0.5
    newGreen = getGreen(p) * 1.2 
    newBlue = getBlue(p) * 0.5
    setColor(p, makeColor(newRed, newGreen, newBlue))
  repaint(image)
  
#blue tint
def Blue(image):
  for p in getPixels(image):
    newRed = getRed(p) * 0.2
    newGreen = getGreen(p) * 0.4
    newBlue = getBlue(p) * 1.2
    setColor(p, makeColor(newRed, newGreen, newBlue))
  repaint(image)
    
#purple tint
def Purple(image):
  for p in getPixels(image):
    newRed = getRed(p) * 0.9
    newGreen = getGreen(p) * 0.5
    newBlue = getBlue(p) * 1.4
    setColor(p, makeColor(newRed, newGreen, newBlue))
  repaint(image)

#grayscale callback function
#no parameters
def grayScaleCB(): #code for this function is in the textbook
  for p in getPixels(image):
    newRed = getRed(p) * 0.299 #colors weighted for eyes perception of luminance
    newGreen = getGreen(p) * 0.587
    newBlue = getBlue(p) * 0.114
    luminance = newRed + newGreen + newBlue #averages color values
    setColor(p, makeColor(luminance, luminance, luminance))
  repaint(image)

#grayscale function for sepia filter
#one parameter
def grayScaleReg(image): #code for this function is in the textbook
  for p in getPixels(image):
    newRed = getRed(p) * 0.299 #colors weighted for eyes perception of luminance
    newGreen = getGreen(p) * 0.587
    newBlue = getBlue(p) * 0.114
    luminance = newRed + newGreen + newBlue #averages color values
    setColor(p, makeColor(luminance, luminance, luminance))
  repaint(image)
  
#inverted color callback function
def invColor():
  for p in getPixels(image):
    newRed = 255 - getRed(p) 
    newGreen = 255 - getGreen(p)
    newBlue = 255 - getBlue(p)
    setColor(p, makeColor(newRed, newGreen, newBlue))
  repaint(image)

#sepia film callback function
def SepiaFil(): #code for this function is in the textbook
  grayScaleReg(image) #first makes picture grayscale
  for p in getPixels(image):
    red1 = getRed(p)
    blue1 = getBlue(p)
    
    if red1 < 63: #tint shadows
      red1 = red1 * 1.1
      blue1 = blue1 * 0.9
    
    if 63 < red1 < 192: #tint midtones
      red1 = red1 * 1.15
      blue1 = blue1 * 0.85
      
    if red1 > 192: #tint highlights
      red1 = red1 * 1.08
      if red1 > 255:
        red1 = 255   
      blue1 = blue1 * 0.93
 
    setRed(p, red1)
    setBlue(p, blue1)  
  repaint(image)
        
#polaroid border callback function
def polaroidFil():
  canvas = makeEmptyPicture (getWidth(image)+40, getHeight(image)+120, white)
  copyInto(image, canvas, 20, 20) #adds white border around picture
  addRect(canvas, 20, 20, getWidth(image), getHeight(image), black) #adds black outline around image
  show(canvas) #will create a new object because it will show canvas rather than image

#color filter callback function
def selectColor():
  color = requestString('Select a Color: red, orange, yellow, green, blue, purple') #user selects a color
  if color == 'red': 
    Red(image) #red tint function
  if color == 'orange':
    Orange(image) #orange tint function
  if color == 'yellow': 
    Yellow(image) #yellow tint function
  if color == 'green':
    Green(image) #green tint function
  if color == 'blue':
    Blue(image) #blue tint function
  if color == 'purple':
    Purple(image) #purple tint function
  
#save callback function
def saveImage():
  path = requestString ('What path do you want to save the image to?') #asks user for a path
  writePictureTo(image, path) #saves picture to user's path

#reset callback function
def resetImage():
  global orig, image
  for x in range(getWidth(image)):
    for y in range(getHeight(image)): #runs through all pixels in orig and copies them to image
      originalPixel = getPixelAt(orig, x, y)
      newPixel = getPixelAt(image, x, y)
      setColor(newPixel, getColor(originalPixel))
  repaint(image)

#create buttons using callback functions
selectImage = gui.Button ('Select Image', selectImage)
grayScale = gui.Button('Grayscale', grayScaleCB)
invColor = gui.Button('Inverted Colors', invColor)
sepiaFil = gui.Button('Sepia Filter', SepiaFil)
polaroidFil = gui.Button('Polaroid Filter', polaroidFil)
colorFil = gui.Button ('Color Filter', selectColor)
save = gui.Button ('Save Image', saveImage)
reset = gui.Button ('Reset Image', resetImage)

#add buttons to gui panel
disp.add (selectImage, 40, 20)
disp.add (grayScale, 50, 100)
disp.add (invColor, 35, 180)
disp.add (sepiaFil, 45, 260)
disp.add (polaroidFil, 36, 340)
disp.add (colorFil, 42, 420)
disp.add (reset, 40, 500)
disp.add (save, 45, 580)



