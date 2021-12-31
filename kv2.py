import kivy
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self, ):  # since we defined inside class by default we dont need to pass "instsance" to the function
        print("name: ", self.name.text, "\nEmail", self.email.text)
        self.name.text = " "
        self.email.text = " "


class DemoApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    DemoApp().run()
