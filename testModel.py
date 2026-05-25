from model.model import Model

modello = Model()
stringa = modello.creaGrafo(2015)
stringa1 = modello.dettagli(2776)
stringa2 = modello.percorso(2776)
print(stringa)
print(stringa1)
print(stringa2)