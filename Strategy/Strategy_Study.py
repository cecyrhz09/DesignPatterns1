'''
Created on 23 nov. 2019

@author: Cecy Rodríguez
'''
from types import MethodType

class Student(object):
    
    def __init__(self, *args, **kwargs):
        self.name = kwargs.pop('name', None) or 'Student'
        if kwargs.get('study', None):
            self.study = MethodType(kwargs.pop('study'), self)

    def study(self):
        
        message = '{} should implement a study method'.format(
            self.__class__.__name__)
        raise NotImplementedError(message)
    

class StudentA(Student):  
    def StudentA_study(self):
        print('I am reading because I am a {}.'.format(self.name))
        

class StudentB(Student):
    def StudentB_study(self):
        print('I am making mind map because  I am a(n) {}.'.format(self.name))

class StudentC(Student):
    def StudentC_study(self):
        print('I am watching videos because I am a {}.'.format(self.name))
    


generic_student = Student()
instintivo_student= Student(name='Dedicated Student', study=StudentA)
visual_student  = Student(name='Visual Student', study=StudentB)
auditory_student = Student(name='Auditory Student', study=StudentC)

instintivo_student.study()
visual_student.study()
auditory_student.study()
