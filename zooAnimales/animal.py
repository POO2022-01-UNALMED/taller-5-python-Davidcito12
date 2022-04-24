class Animal:
    _totalAnimales = 0
    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, zona=None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal._totalAnimales += 1

    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        return f'Mamiferos: {Mamifero.cantidadMamiferos()}\nAves: {Ave.cantidadAves()}\nReptiles: {Reptil.cantidadReptiles()}\n' \
               f'Peces: {Pez.cantidadPeces()}\nAnfibios: {Anfibio.cantidadAnfibios()}'

    @classmethod
    def movimiento(cls):
        return "desplazarse"

    def __str__(self):
        if self._zona!= None:
            return f'Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat}, ' \
                   f'y mi genero es {self._genero}, la zona en la que me ' \
                   f'ubico es {self._zona.getNombre()}, en el {self._zona.getZoo().getNombre()}'

    @classmethod
    def getTotalAnimales(cls):
        return Animal._totalAnimales

    @classmethod
    def setTotalAnimales(cls, nuevoTotal):
        Animal._totalAnimales = nuevoTotal

    def getNombre(self):
        return self._nombre

    def setNombre(self, nuevoNombre):
        self._nombre = nuevoNombre

    def getEdad(self):
        return self._edad

    def setEdad(self, nuevaEdad):
        self._edad = nuevaEdad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self, nuevoHabitat):
        self._habitat = nuevoHabitat

    def getGenero(self):
        return self._genero

    def setGenero(self, nuevoGenero):
        self._genero = nuevoGenero

    def getZona(self):
        return self._zona

    def setZona(self, nuevaZona):
        self._zona = nuevaZona