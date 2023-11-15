import pyautogui   
import pyscreeze
import time
import keyboard



while True:
    im=pyautogui.screenshot()
    screen=im.getpixel((140,219))

    x1=im.getpixel((726,328))
    x2=im.getpixel((723,328))
    x3=im.getpixel((715,328))
    x4=im.getpixel((695,328))
    x5=im.getpixel((605,328))
    x6=im.getpixel((695,328))

    y1=im.getpixel((752,308))
    y2=im.getpixel((765,308))
    y3=im.getpixel((723,308))
    y4=im.getpixel((705,308))
    y5=im.getpixel((715,308))
    y6=im.getpixel((725,308))

    if screen[0]==255:
        if x1[0]!=255 or x2[0]!=255 or x3[0]!=255 or x4[0]!=255 or x5[0]!=255 or x6[0]!=255 or y1[0]!=255 or y2[0]!=255 or y3[0]!=255 or y3[0]!=255 or y4[0]!=255 or y5[0]!=255 or y6[0]!=255:
            pyautogui.press('space')
            time.sleep(0.00001)
        
    else:
        if x1[0]!=32 or x2[0]!=32 or x3[0]!=32 or x4[0]!=32 or x5[0]!=32 or x6[0]!=32 or y1[0]!=32 or y2[0]!=32 or y3[0]!=32 or y4[0]!=32 or y5[0]!=32 or y6[0]!=32: 
            pyautogui.press('space')
            time.sleep(0.00001)
            
            

    if keyboard.is_pressed('s'):
        break

    else:
        pass
        
        
        
