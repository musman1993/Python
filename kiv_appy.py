import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
# comment: 
    
class MyGridLayout(GridLayout):
#initialize infinite keywords
    
    def __init__ (self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        
        self.cols = 2
        
        self.add_widget(Label(text="Name: "))


class MyApp(App):
    def build(self):
        return Label(text="KIVY")
    
    
if __name__ =="__main__":
    MyApp().run()