from guizero import App
from guizero import PushButton
from guizero import Picture
from guizero import Text
from playsound import playsound
import time
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.IN) #set the GPIO pin for PIR sensor as input


#def say_my_name():
    #welcome_message.value = my_name.value
def button1_pressed():
    playsound("/home/bruttherjoe/Desktop/BIG DESIGN ENERGY/FREE Air Horn Sound.mp3")

app = App(layout="grid")
button1 = PushButton(app, image = "Medication Thumbnail.png", grid=[0,0], command=button1_pressed)
button2 = PushButton(app, image = "Expenditure Thumbnail.png", grid=[1,0])
button3 = PushButton(app, image = "Appointments Thumbnail.png", grid=[2,0])
button4 = PushButton(app, image = "Records Thumbnail.png", grid=[0,1])
button5 = PushButton(app, image = "Exercises Thumbnail.png", grid=[1,1])
button6 = PushButton(app, image = "Settings Thumbnail.png", grid=[2,1])

#try:
while True: #indefinitely check for motion
 #   input=GPIO.input(2) #set the current value received by PIR sensor
  #  if input==0:
   #     time.sleep(80)
    #elif input==1:
     #   playsound("/home/bruttherjoe/Desktop/BIG DESIGN ENERGY/FREE Air Horn Sound.mp3") # play the airhorn sound on speaker
        time.sleep(80)
#finally: #If the program is interrupted, this block will be executed
#	GPIO.cleanup() #make sure we are shutting down our program cleanly




#app = App(title="Hello world")
#the header of the program

#button = PushButton(app, image = "cat.gif", align="left")
#the picture nested inside the button

#update_text = PushButton(app, command=say_my_name, text="this is just a test")
#goes with the def command on the top. a button with a text.

#welcome_message = Text(app, text="Welcome to my app")
#random garbo msg at the location

#my_cat = Picture(app, image="cat.gif")
#argument to call a picture.

app.display()
