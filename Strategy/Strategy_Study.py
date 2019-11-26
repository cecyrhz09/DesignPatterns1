'''
Created on 23 nov. 2019

@author: Cecy Rodríguez
'''
from types import MethodType
from abc import ABC, abstractmethod

class Study(ABC):
    
    def __init__(self, *args, **kwargs):
        self.name = kwargs.pop('name', None) or 'Student'
        if kwargs.get('study', None):
            self.study = MethodType(kwargs.pop('study'), self)

    def study(self):
        
        message = '{} should implement a study method'.format(
            self.__class__.__name__)
        raise NotImplementedError(message)
    

class StudentA(Study):  
    def StudentA_study(self):
        print('I am reading because I am a {}.'.format(self.name))
        

class StudentB(Study):
    def StudentB_study(self):
        print('I am making mind map because  I am a(n) {}.'.format(self.name))

class StudentC(Study):
    def StudentC_study(self):
        print('I am watching videos because I am a {}.'.format(self.name))
    

class Client(Study): 
    generic_student = Study()
    instintivo_student= Study(name='Dedicated Student', study=StudentA)
    visual_student  = Study(name='Visual Student', study=StudentB)
    auditory_student = Study(name='Auditory Student', study=StudentC)

    instintivo_student.study()
    visual_student.study()
    auditory_student.study()
