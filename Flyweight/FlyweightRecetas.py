'''
Created on 25 nov. 2019

@author: Cecy Rodríguez
'''
'''
Created on 23 nov. 2019

@author: Cecy Rodríguez
'''

from abc import ABC, abstractmethod


class RecetasFactory:
    def __init__(self):
        self.recetas = {}

    def get_recetas(self, key):
        try:
            receta = self.recetas[key]
        except KeyError:
            receta = ConcreteReceta()
            self.recetas[key] = receta
        return receta


class Receta(ABC):

    def __init__(self):
        self.name = None

    @abstractmethod
    def calcularCosto(self, venta):
        pass


class ConcreteReceta(Receta):
    

    def calcularCosto(self, venta):
        Receta.calcularCosto(self, venta)

class Client():
    def comprar(self):
        receta_factory = RecetasFactory()
        concrete_flyweight = receta_factory.get_recetas("key")
        concrete_flyweight.calcularCosto(None)


c = Client()
c.comprar()