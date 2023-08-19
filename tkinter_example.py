'''
This is a handy tkinter example that uses classes.
It makes it much easier to pass variables around and avoids the use of the global keyword.


'''



import tkinter as tk

class MyGUI:
    def __init__(self):
        # Create main window
        self.root = tk.Tk()
        self.root.title("My GUI")
        self.root.geometry("400x300")

        # Widgets
        self.label = tk.Label(self.root, text=f"nothing has been said")
        self.button_01 = tk.Button(self.root, text="hello", command=self.button_click_01)
        self.button_02 = tk.Button(self.root, text="goodbye", command=self.button_click_02)
        self.entry = tk.Entry(self.root)
        
        # Layout
        self.label.pack()
        self.button_01.pack()
        self.button_02.pack()
        self.entry.pack()

        self.counter = 0 
        

    def button_click_01(self):
        ''' the button is clicked '''
        value = self.entry.get()
        self.label.config(text=f'hello world ! {self.counter} .. {value}')
        self.counter += 1

    def button_click_02(self):
        ''' the button is clicked '''
        self.label.config(text=f'goodbye... {self.counter}')
        self.counter += 1
        
    def start(self):
        self.root.mainloop()

# Usage
app = MyGUI()
app.start()

