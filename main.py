# Step 1 - Create the App
# Step 2 - Create the Game
# Step 3 - Build the Game
# Step 4 - Run the App

from kivy.app import App
from kivy.uix.widget import Widget

class PongGame(Widget):
    pass

class PongApp(App):
    def build(self):
        return PongGame()

PongApp().run()