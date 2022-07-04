from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivymd import images_path
from kivy.clock import Clock
from kivy.core.window import Window


class HomeScreen(BoxLayout):
    sm_1 = ObjectProperty()
    sm_2 = ObjectProperty()
    sm_3 = ObjectProperty()
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)
        # self.ids.toolbar.ids.label_title.font_name = "assets/font/Daniel Davis.ttf"
        # self.ids.toolbar.ids.label_title.font_size = '50sp'

    def _key_handler(self, instance, key, *args):
        if key is 27:
            print('home')
            self.set_previous_screen()

            return True

    def set_previous_screen(self):
        if self.sm_1.current != 'screen_one_name':
            self.sm_1.transition.direction = 'right'
            self.sm_1.current = self.sm_1.previous()
        elif self.sm_3.current != 'screen_three_name':
            self.sm_3.transition.direction = 'right'
            self.sm_3.current = self.sm_3.previous()
        # elif self.sm_3.current != 'screen_three_name':
        #     self.sm_3.transition.direction = 'right'
        #     self.sm_3.current = self.sm_3.previous()