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
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    ''' class for the buttons and widgets '''

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text='first name: '))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text='last name: '))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text='email: '))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text='submit', font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        print('pressed')
        name = self.name.text
        last = self.lastName.text
        email = self.email.text

        print('first name:',name)
        print('last name', last)
        print('email:', email)

        self.name.text = ''
        self.lastName.text = ''
        self.email.text = ''

class SomeApp(App):
    ''' kivy class '''

    def build(self):
        #return Label(text='hello world')
        return MyGrid()




if __name__ == "__main__":
    SomeApp().run()

