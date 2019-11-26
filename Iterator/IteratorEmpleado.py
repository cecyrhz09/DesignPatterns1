'''
Created on 23 nov. 2019

@author: Cecy Rodríguez
'''

from abc import ABC, abstractmethod


class Iterator(ABC):
    
    @abstractmethod
    def has_next(self):
        pass 

    @abstractmethod
    def next(self):
        pass
    
class Iterable(Iterator): 
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
    
ITERABLE =  Iterable()

while ITERABLE.has_next():
    print(ITERABLE.next())
        
