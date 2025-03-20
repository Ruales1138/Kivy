from kivy.app import App
from kivy.uix.label import Label

class HelloApp(App):
    def build(self):
        nombre = 'David'
        label = Label(
            text=f"Hola {nombre}",
            font_size=50,
            color=('#75ff33')
            )
        return label

if __name__ == "__main__":
    HelloApp().run()