from .animal import Animal
class Ave:
    halcones=0
    aguilas=0
    _listado=[]
    def __init__(self,nombre,edad,habitat,genero,colorPlumas=None):
        super().__init__(nombre,edad,habitat,genero)
        self._colorPlumas=colorPlumas
        self._listado.append(self)
        
    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
        
    def getListado(self):
        return self._listado
    
    def setListado(self, listado):
        self._listado = listado
    @classmethod
    def crearHalcon(cls, nombre = "", edad = 0, genero = ""):
        halcon = Ave(nombre, edad, "montanas", genero,"cafe glorioso")
        cls.halcones += 1
        return halcon
    @classmethod
    def cantidadAves(cls):
        return len(cls._listado)
    @classmethod
    def crearAguila(cls, nombre = "", edad = 0, genero = ""):
        aguilas = Ave(nombre, edad, "montanas", genero,"blacno y amarillo")
        cls.aguilas += 1
        return aguilas
    def movimiento(self):
        return "volar"
