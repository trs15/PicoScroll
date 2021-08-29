import picoscroll
import random

# Initialise the board
picoscroll.init()

#Get the width and height of the board
width = picoscroll.get_width()
height = picoscroll.get_height()

#Loop forever
while True:
  #If the A button is pressed light a random LED at a random brightness 
  if(picoscroll.is_pressed(picoscroll.BUTTON_A) == True):
      randX = random(range(0,width-1))
      randY = random(range(0,height-1))
      randB = random(range(0,255))
      picoscroll.set_pixel(randX, randY, randB)

  #If the B button ist pressed turn off all LEDs
  if(picoscroll.is_pressed(picoscroll.BUTTON_A) == True):
      picoscroll.clear()
  
  picoscroll.update()