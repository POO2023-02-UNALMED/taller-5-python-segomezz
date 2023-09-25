from .animal import Animal
class Mamifero(Animal):
    caballo=0
    leones=0
    _listado=[]
    def __init__(self,nombre,edad,habitat,genero,pelaje=False,patas=0):
        super().__init__(nombre,edad,habitat,genero)
        self._pelaje=pelaje
        self._patas=patas
        self._listado.append(self)
    def isPelaje(self):
        return self._pelaje
    
    def setPelaje(self, pelaje):
        self._pelaje = pelaje
        
    def getPatas(self):
        return self._patas
    
    def setPatas(self, patas):
        self._patas = patas
        
    def getListado(self):
        return self._listado
    
    def setListado(self, listado):
        self._listado = listado
    @classmethod
    def crearCaballo(cls, nombre = "", edad = 0, genero = ""):
        caballo = Mamifero(nombre, edad, "pradera", genero, True, 4)
        cls.caballos += 1
        return caballo
    @classmethod
    def cantidadMamiferos(cls):
        return len(cls._listado)
    @classmethod
    def crearLeon(cls, nombre = "", edad = 0, genero = ""):
        leon = Mamifero(nombre, edad, "selva", genero, True, 4)
        cls.leones += 1
        return leon