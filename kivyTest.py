'''

need to do this for kivy to work:
    python -m pip install kivy==2.0.0rc1

this older version fails
    python -m pip install kivy==1.11.1


by: @dlefcoe

'''

import kivy


print(f'the version of kivy is: {kivy.__version__}')

from kivy.app import App
from kivy.uix.label import Label

class SomeApp(App):
    ''' kivy class '''

    def build(self):
        return Label(text='hello world')





if __name__ == "__main__":
    SomeApp().run()

