import os

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import (BooleanProperty, NumericProperty, ObjectProperty,
                             StringProperty)
from kivy.uix.behaviors import CoverBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

from http_client import HttpClient
from models import Pizza
from storage_manager import StorageManager


class PizzaWidget(BoxLayout):
    name = StringProperty()
    ingredients = StringProperty()
    price = NumericProperty()
    vegetarian = BooleanProperty()
    spicy = BooleanProperty()


class MainWidget(FloatLayout):
    recycleView = ObjectProperty(None)
    error_str = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        """self.pizzas = [
            Pizza(
                "4 cheese",
                "Mozzarella, Emmentaler, Brie, Blue Cheese",
                9.5,
                True,
                False,
            ),
            Pizza(
                "Chorizo",
                "Tomatoes, Chorizo, Pecorino Cheese",
                11.2,
                False,
                True,
            ),
            Pizza(
                "Calzone",
                "Pecorino Cheese, Ham, Mushrooms",
                10,
                False,
                False,
            ),
        ]"""

        HttpClient().get_pizzas(
            self.on_server_data,
            self.on_server_error,
        )

    def on_parent(self, widget, parent):
        pizzas_dict = StorageManager().load_data("pizzas")

        if pizzas_dict:
            self.recycleView.data = pizzas_dict

    def on_server_data(self, pizzas_dict):
        self.recycleView.data = pizzas_dict
        StorageManager().save_data("pizzas", pizzas_dict)

    def on_server_error(self, error):
        print(f"ERROR: {error}")
        self.error_str = f"ERROR: {error}"


kv_path = os.path.join(os.path.dirname(__file__), "pizzascr.kv")
with open(kv_path, encoding='utf8') as f:
    Builder.load_string(f.read())


class PizzaApp(App):
    def build(self):
        return MainWidget()


PizzaApp().run()
