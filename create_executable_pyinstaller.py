import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def hello ():  
    label1 = tk.Label(root, text= 'Hello World!', fg='blue', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)
    
button1 = tk.Button(text='Click Me', command=hello, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()



'''

Steps to Create an Executable using PyInstaller

Step 1: 
    Add Python to Windows Path

    An easy way to add Python to the path is by downloading a
    recent version of Python, and then checking the box to
    'Add Python to PATH' at the beginning of the installation

Step 2:
    Install the PyInstaller Package
    pip install pyinstaller

Step 3:
    create a script.
    Save your Python Script.
    example script above.

Step 4:
    Create the Executable using PyInstaller

    go to the Command Prompt and type:
        cd followed by the location where your 
        Python script is stored.

    then type:
    pyinstaller --onefile pythonScriptName.py

step 5:
    Your executable will be created at the 
    location that you specified

    eg:
    C:\Users\Admin\Desktop\Test

    open the dist folder (which was created).

'''
