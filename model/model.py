import copy
import math
from operator import itemgetter

import networkx as nx

from database.DAO import DAO
from model.arco import Arco


class Model:
    def __init__(self):
        self._G = nx.Graph()
        self._nodi = []
        self._DNodi = {}
        self._archi = []
        self._soluzione = []
        self._tot = 0


    def anni(self):
        return DAO.getAnni()
    def getSquadre(self, anno):
        lista = DAO.getSquadre(anno)
        return lista

    def creaGrafo(self, anno):
        self._G = nx.Graph()
        self._nodi = []
        self._DNodi = {}
        self._archi = []
        nodi = DAO.getSquadre(anno)
        self._G.add_nodes_from(nodi)
        archi = DAO.getArchi(anno)
        for element in nodi:
            self._nodi.append(element)
            self._DNodi[element._ID] = element
        for element in archi:
            nodo1 = self._DNodi[element[0]]
            nodo2 = self._DNodi[element[1]]
            peso = element[2]
            arco = Arco(nodo1, nodo2, peso)
            self._archi.append(arco)
            self._G.add_edge(nodo1, nodo2, weight = peso)
        return(f"Numero nodi {self._G.number_of_nodes()}\n" + f"Numero di archi: {self._G.number_of_edges()}")


    def dettagli(self, squadra):
        nodo = self._DNodi[squadra]
        lista = list(self._G.neighbors(nodo))
        risultati = []
        for element in lista:
            peso = self._G[nodo][element]["weight"]
            tupla = (element, peso)
            risultati.append(tupla)
        risultati.sort(key = itemgetter(1), reverse = True)
        stringa = f"i vicini di {nodo._name} con relativo peso dell'arco"
        for element in risultati:
            stringa = stringa + "\n" + f"{element[1]} - {element[0]._name}"
        return stringa


    def percorso(self, squadra):
        self._soluzione = []
        self._tot = 0
        nodo = self._DNodi[squadra]
        parziale = [nodo]
        arco = math.inf
        tot = 0
        self.itera(nodo, parziale, arco, tot)
        stringa = f"La soluzione ha peso: {self._tot}"
        for i in range(len(self._soluzione)-1):
            stringhetta = f"{self._soluzione[i]._name} --> {self._soluzione[i+1]._name}: {self._G[self._soluzione[i]][self._soluzione[i+1]]["weight"]}"
            stringa = stringa + "\n" + stringhetta
        return stringa


    def itera(self, partenza, parziale, arco, tot):
        print(tot)
        if tot > self._tot:
            self._soluzione = copy.deepcopy(parziale)
            self._tot = tot
        lista = list(self._G.neighbors(partenza))
        for element in lista:
            if element not in parziale:
                archetto = self._G[partenza][element]["weight"]
                if archetto < arco:
                    parziale.append(element)
                    tot1 = tot + archetto
                    self.itera(element, parziale, archetto, tot1)
                    parziale.pop()








