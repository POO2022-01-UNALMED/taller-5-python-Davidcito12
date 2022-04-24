class Zoologico:
    def __init__(self,nombre=None, ubicacion=None):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    def agregarZonas(self,nuevaZona):
        Zoologico._zonas.append(nuevaZona)

    def cantidadTotalAnimales(self):
        contador = 0
        for i in self._zonas:
            contador += i.cantidadAnimales()
        return contador

    def getNombre(self):
        return self._nombre

    def setNombre(self, nuevoNombre):
        self._nombre = nuevoNombre

    def getUbicacion(self):
        return self._ubicacion

    def getZona(self):
        return self._zonas

    def setZona(self, nuevoZonas):
        self._zonas = nuevoZonas