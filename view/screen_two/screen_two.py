from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivymd import images_path
from kivy.clock import Clock
# Importing Drop-down from the module to use in the program
from kivy.uix.dropdown import DropDown

# The Button is a Label with associated actions
# that are triggered when the button is pressed
# (or released after a click / touch)
from kivymd.uix.button import MDRaisedButton

# another way used to run kivy app
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.properties import StringProperty

from kivymd.uix.list import OneLineIconListItem
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
class Content(MDBoxLayout):
    '''Custom content.'''
class IconListItem(OneLineIconListItem):
    icon = StringProperty()

class ScreenTwo(Screen):
    field_kecerahan = ObjectProperty()
    field_salinitas = ObjectProperty()
    field_ph        = ObjectProperty()
    # toolbar         = ObjectProperty()
    hasil           = StringProperty()
    hasil_kec       = StringProperty()
    hasil_sal       = StringProperty()
    hasil_ph        = StringProperty()
    
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.on_start, 0)

    def on_start(self, tm=1):
        # self.ids.toolbar.label_title.font_name = "assets/font/Daniel Davis.ttf"
        # self.ids.toolbar.label_title.font_size = '50sp'
        menu_items_kecerahan = [
            {
                "viewclass": "IconListItem",
                "icon": "brightness-7",
                "height": dp(56),
                "text": f"{i}",
                "on_release": lambda x=f"{i}": self.set_item_kec(x),
            } for i in range(50)]
        self.menu_kecerahan = MDDropdownMenu(
            caller=self.ids.field_kecerahan,
            items=menu_items_kecerahan,
            position="bottom",
            width_mult=4,
        )


        menu_items_salinitas = [
            {
                "viewclass": "IconListItem",
                "icon": "alpha-s-circle-outline",
                "height": dp(56),
                "text": f"{i}",
                "on_release": lambda x=f"{i}": self.set_item_sal(x),
            } for i in range(50)]
        self.menu_salinitas = MDDropdownMenu(
            caller=self.ids.field_salinitas,
            items=menu_items_salinitas,
            position="bottom",
            width_mult=4,
        )


        nilai_ph = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3
, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7
, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1
, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5
, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9
, 7.0, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8.0, 8.1, 8.2, 8.3
, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9, 9.0, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7
, 9.8, 9.9, 10.0, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 10.9, 11.0, 11.1
, 11.2, 11.3, 11.4, 11.5, 11.6, 11.7, 11.8, 11.9, 12.0, 12.1, 12.2, 12.3, 12.4, 12.5
, 12.6, 12.7, 12.8, 12.9, 13.0, 13.1, 13.2, 13.3, 13.4, 13.5, 13.6, 13.7, 13.8, 13.9, 14.0]
        menu_items_ph = [
            {
                "viewclass": "IconListItem",
                "icon": "alpha-p-circle-outline",
                "height": dp(56),
                "text": f"{i}",
                "on_release": lambda x=f"{i}": self.set_item_ph(x),
            } for i in nilai_ph]
        self.menu_ph = MDDropdownMenu(
            caller=self.ids.field_ph,
            items=menu_items_ph,
            position="bottom",
            width_mult=4,
        )

    def set_item_kec(self, text__item):
        self.ids.field_kecerahan.text = text__item
        print(text__item)
        self.menu_kecerahan.dismiss()
    
    def set_item_sal(self, text__item):
        self.ids.field_salinitas.text = text__item
        print(text__item)
        self.menu_salinitas.dismiss()    

    def set_item_ph(self, text__item):
        self.ids.field_ph.text = text__item
        print(text__item)
        self.menu_ph.dismiss()

    def proses(self, kecerahan, salanitas, ph):
        hasil='null'
        kecerahan0  = int(kecerahan)
        salanitas0  = int(salanitas)
        ph0         = float(ph)

        kecerahan_normal = 8 - kecerahan0
        salinitas_normal = 31 - salanitas0
        ph_normal        = 5.6 - ph0

        if kecerahan0 > 6 and kecerahan0 < 41 and salanitas0 > 30 and salanitas0 < 36 and ph0 > 5.4 and ph0 < 7.6:
            hasil = 'Sangat Baik'
            # hasil = '(14) Sangat Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            # 14

        elif kecerahan0 < 7 and salanitas0 > 30 and salanitas0 < 36 and ph0 < 5.4:
            hasil = 'Tidak Baik'
            # hasil = '(4) Tidak Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 4

        elif kecerahan0 > 6 and kecerahan0 < 41 and salanitas0 > 30 and salanitas0 < 36 and ph0 < 5.4:
            hasil = 'Baik'
            # hasil = '(13) Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 13

        elif kecerahan0 > 6 and kecerahan0 < 41 and salanitas0 > 30 and salanitas0 < 36 and ph0 > 7.5:
            hasil = 'Baik'
            # hasil = '(15) Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 15

        elif kecerahan0 > 6 and kecerahan0 < 41 and salanitas0 > 35 and ph0 >5.4 and ph0 <7.6:
            hasil = 'Baik'
            # hasil = '(17) Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 17

        elif kecerahan0 > 6 and kecerahan0 < 41 and salanitas0 < 29 and ph0 > 5.4 and ph0 < 7.6:
            hasil = 'Baik'
            # hasil = '(11) Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 11

        elif kecerahan0 > 40 and salanitas0 > 30 and salanitas0 < 36 and ph0 >5.4 and ph0 <7.6:
            hasil = 'Baik' 
            # hasil = '(23) Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 23

        elif kecerahan0 < 7 and salanitas0 > 30 and salanitas0 < 36 and ph0 > 5.4 and ph0 < 7.6:
            hasil = 'Baik'
            # hasil = '(5) Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 5


        elif kecerahan0 > 6 and kecerahan0 < 41 and salanitas0 < 29 and ph0 < 5.4:
            hasil = 'Tidak Baik'
            # hasil = '(10) Tidak Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 10

        elif kecerahan0 > 6 and kecerahan0 < 41 and salanitas0 < 35 and ph0 >7.5:
            hasil = 'Sangat Sangat Baik'
            # hasil = '(18) Sangat Sangat Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 18


        elif kecerahan0 < 7 and salanitas0 > 30 and salanitas0 < 36 and ph0 > 7.5:
            hasil = 'Sangat Tidak Baik'
            # hasil = '(6) Sangat Tidak Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 6

        elif kecerahan0 > 6 and kecerahan0 < 41 and salanitas0 < 29 and ph0 > 7.5:
            hasil = 'Sangat Tidak Baik'
            # hasil = '(12) Sangat Tidak Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 12

        elif kecerahan0 > 6 and kecerahan0 < 41 and salanitas0 > 35 and ph0 <5.4:
            hasil = 'Tidak Baik'
            hasil = '(16) Tidak Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 16


        elif kecerahan0 > 40 and salanitas0 > 30 and salanitas0 < 36 and ph0 <5.4:
            hasil = 'Tidak Baik'
            # hasil = '(22) Tidak Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 22


        elif kecerahan0 > 40 and salanitas0 > 30 and salanitas0 < 36 and ph0 >7.5:
            hasil = 'Tidak Baik'
            # hasil = '(24) Tidak Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 24

        elif kecerahan0 < 7 and salanitas0 > 35 and ph0 > 5.4 and ph0 < 7.6:
            hasil = 'Tidak Baik'
            # hasil = '(8) Tidak Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 8

        elif kecerahan0 > 40 and salanitas0 > 35 and ph0 > 5.4  and ph0 < 7.6:
            hasil = 'Tidak Baik'
            # hasil = '(26) Tidak Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 26

        elif kecerahan0 > 40 and salanitas0 < 29 and ph0 >5.4 and ph0 <7.6:
            hasil = 'Tidak Baik'
            # hasil = '(20) Tidak Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 20

        elif kecerahan0 < 7 and salanitas0 < 29 and ph0 < 5.4:
            hasil = 'Sangat Tidak Baik'
            # hasil = '(1) Sangat Tidak Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 1

        elif kecerahan0 < 7 and salanitas0 < 29 and ph0 > 7.5:
            hasil = 'Sangat Tidak Baik'
            # hasil = '(3) Sangat Tidak Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 3

        elif kecerahan0 < 7 and salanitas0 < 29 and ph0 > 5.4:
            hasil = 'Tidak Baik'
            # hasil = '(2) Tidak Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 2


        elif kecerahan0 < 7 and salanitas0 > 35 and ph0 < 5.4:
            hasil = 'Sangat Tidak Baik'
            # hasil = '(7) Sangat Tidak Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 7

        elif kecerahan0 < 7 and salanitas0 < 35 and ph0 > 7.5:
            # hasil = 'Sangat Tidak Baik'
            # hasil = '(9) Sangat Tidak Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 9


        elif kecerahan0 > 40 and salanitas0 < 29 and ph0 <5.4:
            hasil = 'Sangat Tidak Baik'
            # hasil = '(19) Sangat Tidak Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 19


        elif kecerahan0 > 40 and salanitas0 < 29 and ph0 >7.5:
            hasil = 'Sangat Tidak Baik'
            # hasil = '(21) Sangat Tidak Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 21



        elif kecerahan0 > 40 and salanitas0 > 35 and ph0 < 5.4:
            hasil = 'Sangat Tidak Baik'
            # hasil = '(25) Sangat Tidak Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 25


        elif kecerahan0 > 40 and salanitas0 < 35 and ph0 > 7.5:
            hasil = 'Tidak Baik'
            # hasil = '(27) Tidak Baik'
            hasil_kec = f"{int(kecerahan_normal)}"
            hasil_sal = f"{int(salinitas_normal)}"
            hasil_ph  = f"{int(ph_normal)}"
            self.ids.hasil.text = hasil
            self.ids.hasil_kec.text = hasil_kec
            self.ids.hasil_sal.text = hasil_sal
            self.ids.hasil_ph.text = hasil_ph
            self.ids.hasil.text = hasil
            # 27

        else:
            hasil = 'null'
            print('null')
            self.ids.hasil.text = hasil