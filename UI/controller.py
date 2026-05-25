import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def popola(self, e):
        self._view._txtSquadre.controls.clear()
        self._view._ddSquadra.options.clear()
        anno = self._view._ddAnno.value
        if anno is None:
            stringa = ft.Text("NON HAI SELEZIONATO UN ANNO", color = "red")
            self._view._txtSquade.controls.append(stringa)
            self._view.update_page()
            return
        lista = self._model.getSquadre(int(anno))
        stringa = ft.Text(f"Ho trovato {len(lista)} squadre pèer l'anno {anno}")
        self._view._txtSquadre.controls.append(stringa)
        for element in lista:
            stringa = ft.Text(element._teamCode)
            self._view._txtSquadre.controls.append(stringa)
            opzione = ft.dropdown.Option(text=f"{element._teamCode}", key = f"{element._ID}")
            self._view._ddSquadra.options.append(opzione)
        self._view._btnDettagli.disabled=True
        self._view._btnPercorso.disabled = True
        self._view.update_page()

    def handleCreaGrafo(self, e):
        self._view._txt_result.controls.clear()
        anno = self._view._ddAnno.value
        if anno is None:
            stringa = ft.Text("NON HAI SELEZIONATO UN ANNO", color="red")
            self._view._txt_result.controls.append(stringa)
            self._view.update_page()
            return
        self._model.creaGrafo(int(anno))
        self._view._btnDettagli.disabled=False
        self._view.update_page()

    def handleDettagli(self, e):
        self._view._txt_result.controls.clear()
        squadra = self._view._ddSquadra.value
        if squadra is None or squadra == "":
            stringa = ft.Text("NON HAI SELEZIONATO UNA SQUADRA", color="red")
            self._view._txt_result.controls.append(stringa)
            self._view.update_page()
            return
        stringa = self._model.dettagli(int(squadra))
        self._view._txt_result.controls.append(ft.Text(stringa))
        self._view._btnPercorso.disabled= False
        self._view.update_page()


    def anni(self):
        lista = self._model.anni()
        for element in lista:
            opzione = ft.dropdown.Option(element[0])
            self._view._ddAnno.options.append(opzione)
        self._view.update_page()

    def handlePercorso(self, e):
        self._view._txt_result.controls.clear()
        squadra = self._view._ddSquadra.value
        if squadra is None or squadra == "":
            stringa = ft.Text("NON HAI SELEZIONATO UNA SQUADRA", color="red")
            self._view._txt_result.controls.append(stringa)
            self._view.update_page()
            return
        stringa = self._model.percorso(int(squadra))
        self._view._txt_result.controls.append(ft.Text(stringa))
        self._view.update_page()

