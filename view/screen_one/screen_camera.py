from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivymd import images_path
from kivy.clock import Clock
import time

class Content(MDBoxLayout):
    '''Custom content.'''

class ScreenCamera(Screen):
    # def capture(self):
    #     '''
    #     Function to capture the images and give them the names
    #     according to their captured time and date.
    #     '''
    #     camera = self.ids['camera']
    #     timestr = time.strftime("%Y%m%d_%H%M%S")
    #     camera.export_to_png("IMG_{}.png".format(timestr))
    #     print("Captured")
    pass