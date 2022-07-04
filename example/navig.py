from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.list import OneLineIconListItem

from kivy.properties import (
    StringProperty,
    BooleanProperty,
    ObjectProperty,
    NumericProperty,
    ListProperty,
    OptionProperty,
)
Window.size = (330, 660)


kv = '''
#:import MDTextField kivymd.uix.textfield.MDTextField
<MyTile@SmartTileWithLabel>
    size_hint_y: None
    height: "240dp"

<S>:
    MDTextFieldRound:
        pos_hint: {"center_x": .5, "center_y": .95}
        normal_color : [1,1,1,.1]
        color_active : [1,1,1,1]
        size_hint: .8, .07
        hint_text : 'Search a product...'
        icon_left : 'magnify'



<JBSIDIS>
    on_release: app.show_date_picker(root)
    IconLeftWidget:
        icon: "Photos/pro.jpg"

Screen:
    name: "pantalla1"
    MDToolbar:
        id: tb1
        title: "jbsidis"
        pos_hint: {"top": 1}
        md_bg_color: (.1, .1, .5, 1)

    GridLayout:
        cols: 2
        padding: dp(20)
        FloatLayout:
            MDTextFieldRound:
                id: search_field
                pos_hint: {"center_x": .5, "center_y": .87}
                hint_text : 'jbsidis...'
                icon_left : 'magnify'
                normal_color : (100, 100, 50, .5)
                color_active : (255, 255, 255, 0)
                on_text: app.search(root.ids.rvvv9,self.text)

    BoxLayout:
        id: m5
        spacing: dp(10)
        #padding: dp(20)
        pos_hint: {"center_x": .5, "center_y": .32}
        orientation: "vertical"
        BoxLayout:
            id: s_res9
            size_hint_y: None
            height: self.minimum_height
            pos_hint: {"center_x": .5, "center_y": .4}
            orientation: "vertical"
        RecycleView:
            id: rvvv9
            key_viewclass: 'viewclass'
            key_size: 'height'
            RecycleBoxLayout:
                padding: dp(10)
                spacing: dp(5)
                default_size: None, dp(75)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'

    MDToolbar:
        id: success_screen_toolbar
        title: "jbsidis"
        pos_hint: {"top": 1}
        right_action_items: [["progress-check", lambda: print(6)]]


    MDBottomAppBar:
        MDToolbar:
            id: success_screen_bottomappbar
            icon: "magnify"
            on_action_button: app.eq(root.ids.search_field,True)
            type: 'bottom'
            mode: 'center'
            #elevation: '8dp'
            left_action_items: [["calendar-text", lambda x: print(6)], ["account-group", lambda x: print(6)]]
            right_action_items: [["magnify", lambda x: app.eq(root.ids.search_field,True)], ["menu", lambda x: print(6)]]

'''
authors="jbsidis"
class JBSIDIS(OneLineIconListItem):
    datex=StringProperty()
    pass
class blanks1(BoxLayout):
    pass
class S(FloatLayout):
    pass

authors4="jbsidis"
books="""
Austen, Jane (72159) jbsidis
Du Bois, W. E. B. (William Edward Burghardt) (7364) jbsidis
Stowe, Harriet Beecher (7362) jbsidis
Vatsyayana (7343) jbsidis
Schopenhauer, Arthur (7317) jbsidis
Foote, Mary Hallock (7308) jbsidis
Bhide, Shivaram Parashuram (7256) jbsidis
Indrajit, Bhagavanlal (7256) jbsidis
"""
import time
import datetime
class Main(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(kv)
    def get_date(self, date):
        print(date)
        t=str(date).split("-")
        text="[b]"+str(t[-1])+"/"+str(t[1])+"/"+str(t[0])

        year=time.strftime("%Y")
        mes=time.strftime("%m")
        dia=time.strftime("%d")

        bx.text=text
        afecha=str(t[-1])+"/"+str(t[1])+"/"+str(t[0])
                            
        return date
    def show_date_picker(self,b):
        from kivymd.uix.picker import MDDatePicker
        global bx
        bx=b

        yearx=time.strftime("%Y")
        mes=time.strftime("%m")
        dia=time.strftime("%d")

        current=time.strftime("%Y:%m:%d")

        min_date = datetime.datetime.strptime(current, '%Y:%m:%d').date()
        date_dialog = MDDatePicker(
            callback=self.get_date,
            min_date=min_date
            )
        date_dialog.open()

    def all_pdfs(self):
        return books.splitlines()
    def eq(self,a,b):
        a.focus=True
    def search(self,a,b):
        a.data=[]
        for x in self.all_pdfs():
            if b in str(x):
                a.data.append(
                {
                    "viewclass": "JBSIDIS",
                    "markup": True,
                    "text": "[b][size=33]jbsidis: [/b][/size]"+str(x)
                }
                    )
        pass


Main().run()