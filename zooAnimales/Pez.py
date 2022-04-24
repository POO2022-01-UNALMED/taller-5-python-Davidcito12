from Animal import Animal

class Pez(Animal):
    _listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorEscamas=None, cantidadAletas=None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas

    @classmethod
    def cantidadPezes(cls):
        return len(Pez._listado)

    @classmethod
    def crearSalmon(cls,nombre,edad,genero):
        Pez.salmones += 1
        return cls(nombre, edad, "oceano", genero, "rojo", 6)

    @classmethod
    def crearBacalao(cls,nombre,edad,genero):
        Pez.bacalaos += 1
        return cls(nombre, edad, "oceano", genero, "gris", 6)

    @classmethod
    def movimiento(cls):
        return "nadar"

    def getColorEscamas(self):
        return self._colorEscamas

    def setColorPlumas(self, nuevoColor):
        self._colorEscamas = nuevoColor

    def getCantidadAletas(self):
        return self._cantidadAletas

    def setCantidadAletas(self, nuevaCantidad):
        self._cantidadAletas = nuevaCantidad

    @classmethod
    def getListado(cls):
        return Pez._listado

    @classmethod
    def setListado(cls, nuevoListado):
        Pez._listado = nuevoListado