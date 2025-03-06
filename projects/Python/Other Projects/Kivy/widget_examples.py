from kivy.lang import Builder
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.gridlayout import GridLayout


Builder.load_file("widget_examples.kv")


class WidgetsExample(GridLayout):
    counter = 1
    toggle_disabled = BooleanProperty(True)
    my_text = StringProperty(str(counter))
    text_input_str = StringProperty("foo")
    # slider_value_txt = StringProperty("50")

    def on_button_click(self):
        if not self.toggle_disabled:
            self.counter += 1
        # self.counter_text = str(self.counter)
        self.my_text = str(self.counter)

    def on_toggle_state(self, widget):
        print("Toggle state: " + widget.state)

        if widget.state == "normal":
            widget.text = "OFF"
            self.toggle_disabled = True
        else:
            widget.text = "ON"
            self.toggle_disabled = False

    def on_switch_active(self, widget):
        print("Switch active: " + str(widget.active))

    # def on_slider_value(self, widget):
    #     pass
    #     self.slider_value_txt = str(int(widget.value))

    def on_text_validate(self, widget):
        self.text_input_str = widget.text
