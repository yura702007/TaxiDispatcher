from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from driver import Driver


class Container(BoxLayout):

    adress_call = ObjectProperty()
    start_job = ObjectProperty()
    drive_for_client = ObjectProperty()
    waiting_client = ObjectProperty()
    order_execution = ObjectProperty()
    end_job = ObjectProperty()

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

    def waiting_client_method(self):
        """
        Ожидание пассажира
        """
        self.adress_call.text = str(self.dr.waiting_client())

    def order_execution_method(self):
        """
        Везу пассажира
        """
        self.adress_call.text = str(self.dr.order_execution())

    def end_job_method(self):
        with open('file.txt', 'w', encoding='utf8') as file:
            file.write(str(self.dr.end_job()))


class FaceApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    FaceApp().run()
