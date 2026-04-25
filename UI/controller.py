import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # other attributes
        self._mese = 0

    def handle_umidita_media(self, e):
        self._view.lst_result.controls.clear()
        medie = self._model.get_media_umidita(self._mese)

        self._view.lst_result.controls.append(ft.Text("L'umidità nel mese selezionato è:"))
        for m in medie:
            self._view.lst_result.controls.append(ft.Text(f"{m["Localita"]}: {m['Media']}"))
        self._view._page.update()


    def handle_sequenza(self, e):
        mese_selezionato = self._view.dd_mese.value
        self._model.calcola_sequenza(mese_selezionato)

    def read_mese(self, e):
        self._mese = int(e.control.value)

