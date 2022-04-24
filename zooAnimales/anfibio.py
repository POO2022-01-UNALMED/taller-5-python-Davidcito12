from animal import Animal

class Reptil(Animal):
    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorPiel=None, venenoso=None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso

    @classmethod
    def cantidadAnfibios(cls):
        return len(Reptil._listado)

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        Reptil.ranas += 1
        return cls(nombre, edad, "selva", genero, "rojo", True)

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        Reptil.salamandras += 1
        return cls(nombre, edad, "selva", genero, "negro y amarillo", False)

    @classmethod
    def movimiento(cls):
        return "saltar"

    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self, nuevoColor):
        self._colorPiel = nuevoColor

    def isVenenoso(self):
        return self._venenoso

    def setVenenoso(self, nuevoVeneno):
        self._venenoso = nuevoVeneno

    @classmethod
    def getListado(cls):
        return Reptil._listado

    @classmethod
    def setListado(cls, nuevoListado):
        Reptil._listado = nuevoListado