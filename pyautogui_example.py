'''
just an example of pyautogui

'''


import time
import pyautogui

running = True

t0 = time.time()
while running == True:
    time.sleep(0.1)
    t1 = time.time()
    if t1 - t0 > 5:
        running = False
    currentMouseX, currentMouseY = pyautogui.position()
    print(round(t1-t0, 2), currentMouseX, currentMouseY)

screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)
print('done')
