from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivymd import images_path
from kivy.clock import Clock


class Content(MDBoxLayout):
    '''Custom content.'''

class ScreenAbsen(Screen):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")
    def get_link(self, link):
        import webbrowser
        webbrowser.open("https://www.google.com/maps/@-{},15z".format(link))
    def send(self, txt):
        print(txt)
    def on_checkbox_active(self, checkbox, value):
        if value:
            print('The checkbox', checkbox, 'is active', 'and', checkbox.state, 'state')
        else:
            print('The checkbox', checkbox, 'is inactive', 'and', checkbox.state, 'state')
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