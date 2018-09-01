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
    # When a clock object is instantiated by another component,
    # use the kivy Clock module to drive an interrupt every second
    # to update the clock.
    def __init__(self, **kwargs):
        super(DateClock, self).__init__(**kwargs)
        self.text = str(time.asctime())
        Clock.schedule_interval(self.update, 1)

    def update(self, *args):
        self.text = time.asctime()


class CustomPopup(Popup):
    pass


class BigBoxLayout(BoxLayout):
    # A wide array of components all stocked in a BoxLayout.
    # This box stems from widget_demo.
    
    # Track the single checkbox ('Enter')
    checkbox_is_active = ObjectProperty(False)    
    def checkbox_enter_clicked(self, instance, value):
        if value:
            print("Checkbox Checked")
        else:
            print("Not checked")

    # Three booleans for the favorite color group.
    blue = ObjectProperty(True)
    red = ObjectProperty(False)
    green = ObjectProperty(False)

    # Called on switch press.
    def switch_on(self, instance, value):
        if value:
            print("switch on")
        else:
            print("switch off")

    def open_popup(self):
        the_popup = CustomPopup()
        the_popup.open()

    # Called on spinner click.
    def spinner_clicked(self, value):
        print("Spinner " + value)


class ScreenOne(Screen):
    # Updates the Name textfield. 
    # Called by the textInput "on_text_validate" method
    def update_name(self, name):
        self.ids.name_label.text = "Name: " + name
        print("Name: " + name)


class ScreenTwo(Screen):
    # No information needs to be passed between components here
    pass


class ScreenThree(Screen):
    # Change the text to reflect the selected language
    def update_world_label(self, language):
        new_text = 'Hello World'
        if (language == "French"):
            new_text = "Bonjour monde"
        elif (language == "Japanese"):
            new_text = "ハローワールド"
        self.ids.world_label.text = new_text

    # Called on spinner selection
    def spinner_clicked(self, new_language):
        self.update_world_label(new_language)
        print("Spinner " + new_language)


class ThreeScreenApp(App):
    # The application class must end in 'App' with a 
    # prefix == name of the .kv file
    def build(self):
        # Set background
        Window.clearcolor = (1, 1, 1, 1)
        
        # Navigation
        screen_manager = ScreenManager()
        screen_manager.add_widget(ScreenOne(name="screen_one"))
        screen_manager.add_widget(ScreenTwo(name="screen_two"))
        screen_manager.add_widget(ScreenThree(name="screen_three"))
        return screen_manager


sampleApp = ThreeScreenApp()
sampleApp.run()
