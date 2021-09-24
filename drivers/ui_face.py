from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import Property
from driver import dr


class Container(BoxLayout):
    pass


class FaceApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    FaceApp().run()
