from Animal import Animal

class Ave(Animal):
    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorPlumas = None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas= colorPlumas

    @classmethod
    def cantidadAves(cls):
        return len(Ave._listado)

    @classmethod
    def crearHalcon(cls,nombre,edad,genero):
        Ave.halcones += 1
        return cls(nombre,edad,"montanas",genero,"cafe glorioso")

    @classmethod
    def crearAguila(cls,nombre,edad,genero):
        Ave.aguilas += 1
        return cls(nombre, edad, "montanas", genero, "blanco y amarillo")

    @classmethod
    def movimiento(cls):
        return "volar"

    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self, nuevoColor):
        self._colorPlumas = nuevoColor

    @classmethod
    def getListado(cls):
        return Ave._listado

    @classmethod
    def setListado(cls, nuevoListado):
        Ave._listado = nuevoListado