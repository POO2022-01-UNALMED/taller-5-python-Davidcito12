from zooAnimales.animal import Animal

class Mamifero(Animal):
    _listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, pelaje=None, patas=None):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)

    @classmethod
    def cantidadMamiferos(cls):
        return len(Mamifero._listado)

    @classmethod
    def crearCaballo(cls,nombre,edad,genero):
        Mamifero.caballos += 1
        return cls(nombre,edad,"pradera",genero,True, 4)

    @classmethod
    def crearLeon(cls,nombre,edad,genero):
        Mamifero.leones += 1
        return cls(nombre,edad,"selva",genero,True, 4)

    def isPelaje(self):
        return self._pelaje

    def setPelaje(self, nuevoPelaje):
        self._pelaje = nuevoPelaje

    def getPatas(self):
        return self._patas

    def setPatas(self,nuevoPatas):
        self._patas = nuevoPatas

    @classmethod
    def getListado(cls):
        return Mamifero._listado

    @classmethod
    def setListado(cls, nuevoListado):
        Mamifero._listado = nuevoListado