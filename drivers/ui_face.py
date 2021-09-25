from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from driver import Driver


class Container(BoxLayout):
    adress_call = ObjectProperty()
    start_job = ObjectProperty()
    drive_for_client = ObjectProperty

    dr = Driver()

    def start_job_method(self):
        """
        Ожидаю вызова
        """
        self.adress_call.text = str(self.dr.start_job())

    def drive_for_client_method(self):
        """
        Еду за пассажиром
        """
        self.adress_call.text = str(self.dr.drive_for_client())


class FaceApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    FaceApp().run()
