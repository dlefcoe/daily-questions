'''
Example of app using kivy:
the corresponding .kv file is in lower case:
    such that: MyApp => my.kv

need to do this for kivy to work:
    python -m pip install kivy==2.0.0rc1


by: @dlefcoe

'''

# imports
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

print(f'the version of kivy is: {kivy.__version__}')


class MyGrid(Widget):
    ''' class for the buttons and widgets '''
    pass


class MyApp(App):
    ''' inherit kivy class '''

    def build(self):
        #return Label(text='hello world')
        return MyGrid()




if __name__ == "__main__":
    MyApp().run()

