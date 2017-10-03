#person.py
class Person:
    """ Class to represent a person """
    def __init__(self, name = '', age = 0):
        self._name = name
        self.__age = age
        
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 < age <= 150:
            self.__age = age
            
    def display(self):
        print(self)
        
    def __str__(self):
        return "Person('%s', %s)" % (self._name, self.__age)
    
    def __repr__(self):
        return str(self)
    
