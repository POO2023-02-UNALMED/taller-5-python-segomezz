from .animal import Animal
class Reptil:
    serpientes=0
    iguanas=0
    _listado=[]
    def __init__(self,nombre,edad,habitat,genero,colorEscamas=None,largoCola=None):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas=colorEscamas
        self._largoCola= largoCola
        self._listado.append(self)
        
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
        
    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self, largoCola):
        self._largoCola = largoCola
        
    def getListado(self):
        return self._listado
    
    def setListado(self, listado):
        self._listado = listado
    @classmethod    
    def cantidadReptiles():
        return len(Reptil._listado)
    @classmethod
    def crearIguana(cls, nombre = "", edad = 0, genero = ""):
        iguana = Reptil(nombre, edad, "humedal", genero, "verde", 3)
        cls.iguanas += 1
        return iguana
    
    @classmethod
    def crearSerpiente(cls, nombre = "", edad = 0, genero = ""):
        serpiente = Reptil(nombre, edad, "jungla", genero, "blanco", 1)
        cls.serpientes += 1
        return serpiente
    def movimiento(self):
        return "reptar"
