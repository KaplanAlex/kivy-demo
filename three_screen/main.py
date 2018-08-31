import kivy
import time
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.clock import Clock


class DateClock(Label):
    def __init__(self, **kwargs):
        super(DateClock, self).__init__(**kwargs)
        self.text = str(time.asctime())
        Clock.schedule_interval(self.update, 1)

    def update(self, *args):
        self.text = time.asctime()


class CustomPopup(Popup):
    pass


class BigBoxLayout(BoxLayout):

    checkbox_is_active = ObjectProperty(False)

    def checkbox_enter_clicked(self, instance, value):
        if value:
            print("Checkbox Checked")
        else:
            print("Not checked")

    blue = ObjectProperty(True)
    red = ObjectProperty(False)
    green = ObjectProperty(False)

    def switch_on(self, instance, value):
        if value:
            print("switch on")
        else:
            print("switch off")

    def open_popup(self):
        the_popup = CustomPopup()
        the_popup.open()

    def spinner_clicked(self, value):
        print("Spinner " + value)


class ScreenOne(Screen):

    def update_name(self, name):
        self.ids.name_label.text = "Name: " + name
        print("Name: " + name)


class ScreenTwo(Screen):
    pass


class ScreenThree(Screen):

    def update_world_label(self, language):
        new_text = 'Hello World'
        if (language == "French"):
            new_text = "Bonjour monde"
        elif (language == "Japanese"):
            new_text = "ハローワールド"
        self.ids.world_label.text = new_text

    def spinner_clicked(self, new_language):
        self.update_world_label(new_language)
        print("Spinner " + new_language)


class ThreeScreenApp(App):

    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        screen_manager = ScreenManager()

        screen_manager.add_widget(ScreenOne(name="screen_one"))
        screen_manager.add_widget(ScreenTwo(name="screen_two"))
        screen_manager.add_widget(ScreenThree(name="screen_three"))
        return screen_manager


sampleApp = ThreeScreenApp()
sampleApp.run()
