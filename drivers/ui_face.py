from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from driver import Driver


class Container(BoxLayout):
    adress_call = ObjectProperty()
    start_job = ObjectProperty()

    dr = Driver()

    def start_job_method(self):
        self.adress_call.text = str(self.dr.start_job())


class FaceApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    FaceApp().run()
