import kivy
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)



class DemoApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    DemoApp().run()
