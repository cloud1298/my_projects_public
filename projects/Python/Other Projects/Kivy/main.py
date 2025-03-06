from kivy.app import App
from kivy.properties import ObjectProperty

from canvas_examples import *
from navigation_screen_manager import NavigationScreenManager


class MyScreenManager(NavigationScreenManager):
    pass


class TheLabApp(App):
    manager = ObjectProperty(None)

    def build(self):
        self.manager = MyScreenManager()
        return self.manager
        # return CanvasExample7()


TheLabApp().run()
