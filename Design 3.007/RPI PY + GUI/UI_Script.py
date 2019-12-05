

######################### IMPORTANT : ALWAYS SUDO ##################

import keyboard  # using module keyboard
import time
from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('1'):  # pills
            print('You Pressed A Key!')
            # Read pointer position
            ## print('The current pointer position is {0}'.format(mouse.position))
            #time.sleep(1)
            # Set pointer position
            mouse.position = (349,298)
            time.sleep(0.2)
            mouse.press(Button.left)
            time.sleep(0.2)
            mouse.release(Button.left)

        if keyboard.is_pressed('2'):  # stethoscope
            mouse.position = (916,316)
            time.sleep(0.2)
            mouse.press(Button.left)
            time.sleep(0.2)
            mouse.release(Button.left)

        if keyboard.is_pressed('3'):  # money
            mouse.position = (1473, 307)
            time.sleep(0.2)
            mouse.press(Button.left)
            time.sleep(0.2)
            mouse.release(Button.left)

        if keyboard.is_pressed('4'):  # clipboard
            mouse.position = (354, 753)
            time.sleep(0.2)
            mouse.press(Button.left)
            time.sleep(0.2)
            mouse.release(Button.left)

        if keyboard.is_pressed('5'):  # exercise
            mouse.position = (915, 748)
            time.sleep(0.2)
            mouse.press(Button.left)
            time.sleep(0.2)
            mouse.release(Button.left)

        if keyboard.is_pressed('6'):  # settings
            mouse.position = (1469, 740) 
            time.sleep(0.2)
            mouse.press(Button.left)
            time.sleep(0.2)
            mouse.release(Button.left)

            
        if keyboard.is_pressed('0'):  # back button
            mouse.position = (123,57)
            time.sleep(0.2)
            mouse.press(Button.left)
            time.sleep(0.2)
            mouse.release(Button.left)

        if keyboard.is_pressed('+'):  # elderly video
            mouse.position = (1127, 359) 
            time.sleep(0.2)
            mouse.press(Button.left)
            time.sleep(0.2)
            mouse.release(Button.left)

        if keyboard.is_pressed('7'):  # elderly back button
            mouse.position = (1584, 103) 
            time.sleep(0.2)
            mouse.press(Button.left)
            time.sleep(0.2)
            mouse.release(Button.left)

       # if keyboard.is_pressed('q'):  # mousepos
         #   print('You Pressed A Key!')
            # Read pointer position
          #  print('The current pointer position is {0}'.format(mouse.position))
         #   time.sleep(1)
            # Set pointer position


    except:
        break  # if user pressed a key other than the given key the loop will break


 #(1584, 103) for elderly back button
 #(1127, 359) for elderly exercise video
 #(1469, 740) for settings
 #(915, 748) for exercise           
 #(354, 753) for clipboard        
 #(1473, 307) for money           
 #(349,298) for pills
 #(916,316) for stethoscope
 #(123,57) for back button



#Read pointer position
#print('The current pointer position is {0}'.format(
 #   mouse.position))

# Set pointer position
#mouse.position = (10, 20)
#print('Now we have moved it to {0}'.format(
 #   mouse.position))

# Move pointer relative to current position
#mouse.move(5, -5)

# Press and release
##mouse.press(Button.left)
##mouse.release(Button.left)

# Double click; this is different from pressing and releasing
# twice on Mac OSX
##mouse.click(Button.left, 2)

# Scroll two steps down
##mouse.scroll(0, 2)
#                                 =========================================
#from pynput.mouse import Listener

#def on_move(x, y):
    #print('Pointer moved to {0}'.format(
      #  (x, y)))

#def on_click(x, y, button, pressed):
 #   print('{0} at {1}'.format(
  #      'Pressed' if pressed else 'Released',
   #     (x, y)))
    #if not pressed:qqqqqqqqq
        # Stop listener
     #   return False

#def on_scroll(x, y, dx, dy):
 #   print('Scrolled {0}'.format(
  #      (x, y)))

# Collect events until released
#with Listener(
 #       on_move=on_move,
  #      on_click=on_click,
   #     on_scroll=on_scroll) as listener:
    #listener.join()
            #break  # goto finish
        
    
