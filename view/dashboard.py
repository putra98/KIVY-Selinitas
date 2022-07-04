from kivymd.uix.boxlayout import MDBoxLayout 
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.core.window import Window

class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class Dashboard(MDBoxLayout):
    pass
    # sm = ObjectProperty()
    # def __init__(self, **kwargs):
    #     super(Dashboard, self).__init__(**kwargs)
    #     Window.bind(on_keyboard=self._key_handler)
    #     self.ids.toolbar.ids.label_title.font_name = "assets/font/Daniel Davis.ttf"
    #     self.ids.toolbar.ids.label_title.font_size = '50sp'

    # def _key_handler(self, instance, key, *args):
    #     if key is 27:
    #         print('Dashboard')
    #         self.set_previous_screen()
    #         return True

    # def set_previous_screen(self):
    #     if self.sm.current != 'home_name':
    #         self.sm.transition.direction = 'right'
    #         self.sm.current = self.sm.previous()