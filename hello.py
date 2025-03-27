from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class Saludo(App):

    def build(self):
        mi_contenedor=BoxLayout()
        mi_contenedor.orientation ="vertical"
        mi_boton = Button( text="Saludar" )
        self.mi_texto = TextInput()
        self.mi_etiqueta = Label( text="Hola Mundo")
        mi_contenedor.add_widget(self.mi_texto)
        mi_contenedor.add_widget(mi_boton)
        mi_boton.bind(on_press=self.saludar)
        mi_contenedor.add_widget(self.mi_etiqueta)
        return mi_contenedor

    def saludar(self, sender):
        self.mi_etiqueta.text = "Hola "+ self.mi_texto.text
        print("Has llamado al metodo saludar!")

miaplicacion = Saludo()
miaplicacion.run()