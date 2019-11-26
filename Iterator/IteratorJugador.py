'''
Created on 23 nov. 2019

@author: Cecy Rodríguez
'''

from abc import ABC, abstractmethod


class Seleccionador(ABC):
    
    @abstractmethod
    def has_next(self):
        pass 

    @abstractmethod
    def next(self):
        pass
    
class EquipoA(Seleccionador): 
    def __init__(self):
        self.index = 0
        self.maximum = 7
        
    def next(self):
        if self.index< self.maximum:
            x = self.index
            self.index += 1
            return x 
        
        else:
            raise Exception("At the end Iterator Exception")
        
    def has_next(self):
        return self.index < self.maximum

class EquipoB(Seleccionador):
    
    def __init__(self):
        self.index = 0
        self.maximum = 7
       
    def next(self):
        if self.index< self.maximum:
            x = self.index
            self.index += 1
            return x 
        
        else:
            raise Exception("At the end Iterator Exception")
        
    def has_next(self):
        return self.index < self.maximum

class Jugador(Seleccionador): 
    a =  EquipoA()
    b = EquipoB()

    while a.has_next() and b.has_next():
        print(a.next(), b.has_next())
        
