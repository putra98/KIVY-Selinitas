from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

class LoginScreen(Screen):
    data = {
        'Python': 'language-python',
        'PHP': 'language-php',
        'C++': 'language-cpp',
    }
    option = ObjectProperty()

    # def __init__(self, **kwargs):
    #     super(LoginScreen, self).__init__(**kwargs)
    #     speed_dial = MDFloatingActionButtonSpeedDial()
    #     speed_dial.data = self.data
    #     speed_dial.root_button_anim = True
    #     screen.add_widget(speed_dial)

    def option(self, text):
    	print(text)