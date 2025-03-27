from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Triki( App ):
    def build(self):
        self.es_el_primer_jugador = True
        
        tablero = BoxLayout(orientation='vertical')

        for _ in range(3):
            fila = BoxLayout(orientation='horizontal')
            tablero.add_widget(fila)

            for _ in range(3):
                casilla = Button(text='')
                casilla.bind(on_press=self.seleccionar)
                fila.add_widget(casilla)

        return tablero

    def seleccionar(self, sender):
        print(f'Has seleccionado la casilla: {sender.text}')

        if self.es_el_primer_jugador and sender.text == '':
            self.es_el_primer_jugador = not(self.es_el_primer_jugador)
            sender.text = 'X'

        if not self.es_el_primer_jugador and sender.text == '':
            self.es_el_primer_jugador = not(self.es_el_primer_jugador)
            sender.text = 'O'


Triki().run()