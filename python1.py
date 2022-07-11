from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton,MDFloatingActionButton

class MamunApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Green'
        scr = Screen()
        but = MDRectangleFlatButton(text = 'hi',
                           pos_hint={'center_x':0.5,'center_y':.5})

        icon_batton = MDFloatingActionButton(icon='android',pos_hint={'center_x':0.5,'center_y':.5})

        scr.add_widget(icon_batton)
        return scr

MamunApp().run()