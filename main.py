from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon


class MamunApp(MDApp):
    def build(self):
        lable = MDLabel(text='hello wold',halign = 'center',theme_text_color='Custom',
                        text_color=(255/255.0,124/255.0,130/255.01),
                        font_style='H1')
        icon_lab = MDIcon(icon='language-python',halign = 'center')
        return icon_lab


MamunApp().run()
