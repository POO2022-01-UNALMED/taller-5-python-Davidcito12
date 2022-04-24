from zooAnimales.animal import Animal

class Reptil(Animal):
    _listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorEscamas=None, largoCola=None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola

    @classmethod
    def cantidadReptiles(cls):
        return len(Reptil._listado)

    @classmethod
    def crearIguana(cls,nombre,edad,genero):
        Reptil.iguanas += 1
        return cls(nombre, edad, "humedal", genero, "verde", 3)

    @classmethod
    def crearSerpiente(cls,nombre,edad,genero):
        Reptil.serpientes += 1
        return cls(nombre, edad, "jungla", genero, "blanco", 1)

    @classmethod
    def movimiento(cls):
        return "reptar"

    def getColorEscamas(self):
        return self._ColorEscamas

    def setColorEscamas(self, nuevoColor):
        self._ColorEscamas = nuevoColor

    def getLargoCola(self):
        return self._largoCola

    def setLargoCola(self, nuevoLargo):
        self._largoCola = nuevoLargo

    @classmethod
    def getListado(cls):
        return Reptil._listado

    @classmethod
    def setListado(cls, nuevoListado):
        Reptil._listado = nuevoListado