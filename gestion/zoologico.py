
class Zoologico:
    def __init__ (self,nombre=None,ubicacion=None):
        self._nombre=nombre
        self._ubicacion=ubicacion
        self._zonas= []
    def agregarZonas(self,zona):
        self._zonas.append(zona)
    def cantidadTotalAnimales(self):
        totalAnimals=0
        for i in range (len(self._zonas)):
            totalAnimals=0
            totalAnimals+=self._zona[i].cantidadAnimales()
        return totalAnimals
    def getNombre(self):
        return self._nombre
    def getUbicacion(self):
        return self._ubicacion
    def setNombre(self,nombre):
        self._nombre=nombre
    def setUbicacion(self,ubicacion):
        self._ubicacion=ubicacion
