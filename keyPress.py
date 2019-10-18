
import pynput
import time
import random
import winsound

from pynput.keyboard import Key, Controller

frequency = 2500 # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second

keyboard = Controller()


# wait for me to click he window
time.sleep(3)
winsound.Beep(frequency, duration)
print('about to enter the loops')

keyboard.type('hello world')

letterList = ['a','b','c','d','e']

for i in range(10):
    print(f'entering loop number {i+1}')
    # pause for between 1.2 to 2.5 seconds randomly
    r = random.randint(12,25) / 10
    print('sleeping for',r,'seconds')
    time.sleep(r)

    # 3/4 of the time press the left arrow
    if random.random() < 0.75:
        print('pressing left arrow')
        # the left arrow key
        keyboard.press(Key.left)

    else:
        print('did not press left arrow')


    # pause for between 1.5 to 3.5 seconds randomly
    r = random.randint(15,35) / 10
    print('sleeping for',r,'seconds')
    time.sleep(r)

    # 90% of the time press the left arrow
    if random.random() < 0.90:
        print('pressing right arrow')
        # the right arrow key
        keyboard.press(Key.right)

    else:
        print('did not press right arrow')




'''
# single key press examples
keyboard.press('a')
keyboard.press('b')
keyboard.press('>')


keyboard.release('a')
keyboard.type('hello world')
'''




'''


import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


'''