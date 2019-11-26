

from abc import ABC, abstractmethod


class FileFactory:
    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, key):
        try:
            flyweight = self._flyweights[key]
        except KeyError:
            flyweight = ConcreteFile()
            self._flyweights[key] = flyweight
        return flyweight


class File(ABC):

    def __init__(self):
        self.intrinsic_state = None

    @abstractmethod
    def operation(self, extrinsic_state):
        pass


class ConcreteFile(File):
    
    def operation(self, extrinsic_state):
        pass

class Client:
    def have(self):
        flyweight_factory = FileFactory()
        concrete_flyweight = flyweight_factory.get_flyweight("key")
        concrete_flyweight.operation(None)


c = Client()
c.have()
