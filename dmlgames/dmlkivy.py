from kivy.app import App  # type: ignore
from kivy.graphics import Line  # type: ignore
from kivy.uix.gridlayout import GridLayout  # type: ignore
from kivy.uix.label import Label  # type: ignore
from kivy.uix.textinput import TextInput  # type: ignore
from kivy.uix.widget import Widget  # type: ignore

# import kivy                           	# type: ignore
# import os
# from typing import Any

# kivy.require("1.10.0")


class LoginScreen(GridLayout):
	def __init__(self, **kwargs: str) -> None:
		super(LoginScreen, self).__init__(**kwargs)
		self.cols = 2

		self.add_widget(Label(text="Username: "))
		self.username = TextInput(multiline=False)
		self.add_widget(self.username)

		self.add_widget(Label(text="Password: "))
		self.password = TextInput(multiline=False, password=True)
		self.add_widget(self.password)

		self.add_widget(Label(text="Two Factor Auth: "))
		self.tfa = TextInput(multiline=False)
		self.add_widget(self.tfa)


class DrawingApp(Widget):
	def on_touch_down(self, touch):
		# print(touch)
		with self.canvas:
			touch.ud["line"] = Line(points=(touch.x, touch.y))

	def on_touch_move(self, touch):
		# print(touch)
		touch.ud["line"].points += (touch.x, touch.y)

	def on_touch_up(self, touch):
		# print("Released", touch)
		pass


class SimpleKivy(App):
	def build(self):
		# return LoginScreen()
		return DrawingApp()


if __name__ == "__main__":
	SimpleKivy().run()
