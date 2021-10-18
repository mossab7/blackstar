import rotatescreen
import time

def flepscreen():
    screen = rotatescreen.get_primary_display()
    angels = [90,180,270,0]
    for i in angels:
        time.sleep(3)
        screen.rotate_to(i)
        if i == 0:
            break
        
flepscreen()
 


