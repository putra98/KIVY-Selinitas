from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivymd import images_path
from kivy.clock import Clock


class Content(MDBoxLayout):
    '''Custom content.'''

class ScreenEdit(Screen):
    pass
    # box = ObjectProperty()
    
    # def __init__(self, **kw):
    #     super().__init__(**kw)
    #     Clock.schedule_once(self.on_start, 0.5)
    # def on_start(self, tm=1):
    #     for i in range(3):
    #         self.ids.box.add_widget(
    #             MDExpansionPanel(
    #                 icon=f"assets/image/msp2.png",
    #                 content=Content(),
    #                 panel_cls=MDExpansionPanelThreeLine(
    #                     text="Universitas Pelita Bangsa",
    #                     secondary_text="Seminar",
    #                     tertiary_text="25/03/2022 08:37",
    #                 )
    #             )
    #         )