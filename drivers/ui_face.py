from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import Property


class Container(Widget):
    pass


class FaceApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    FaceApp().run()
