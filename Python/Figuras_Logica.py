import math

class Punto:
    def __init__(self):
        int(self.valX)
        int(self.valY)
        int(self.distancia)
        
    def getX(self):
        return self.valX
    def getY (self):
        return self.valY
    
    def setX(self, x):
        self.valX = x
    def setY(self, y):
        self.valY = y

    def calcularDistancia(self, p):
        self.distancia = math.sqrt((self.valX - p.x)**2)+((self.valY - p.y)**2)

    def getDistancia(self):
        return self.distancia

class Figura(Punto):
    def __init__(self):
        self.origen
        self.fin
        int(self.area)
        int(self.perimetro)

    def getOrigen(self):
        return self.origen
    def getFin(self):
        return self.fin

    def setOrigen(self, orgien):
        self.origen = origen
    def setFin(self, fin):
        self.fin = fin

    def calcularArea(self):

        pass
    def getArea(self):
        return self.area

    def calcularPerimetro(self):

        pass
    def getPerimetro(self):
        return self.perimetro

class Circulo(Figura, Punto):
    def __init__(self):
        self.radio = int(origen.calculaDistancia(fin))
        
    def calcularArea(self):
        self.area = int (math.pi*(self.radio**2))
    def calcularPerimetro(self):
        self.perimetro = int((math.pi*2)*self.radio)

class Cuadrado(Figura, Punto):
    def __init__(self):
        self.lado = int(origen.calculaDistancia(fin))
        
    def calcularArea(self):
        self.area = int (self.lado * self.lado)
    def calcularPerimetro(self):
        self.perimetro = int (self.lado * 4)

class Rectangulo(Figura, Punto):
    def __init__(self):
        temp = Figuras_Logica.Punto()
        temp.setX(origen.getX())
        temp.setY(fin.getY())
        self.base = int(temp.calcularDistancia(fin))
        self.altura = int(temp.calcularDistancia(origen))
        
    def calcularArea(self):
        self.area = int (self.base * self.altura)
    def calcularPerimetro(self):
        self.perimetro = int (2 * (self.base + self.altura))

class TrianguloRectangulo(Figura, Punto):
    def __init__(self):
        temp = Figuras_Logica.Punto()
        temp.setX(origen.getX())
        temp.setY(fin.getY())
        self.base = int(temp.calcularDistancia(fin))
        self.altura = int(temp.calcularDistancia(origen))
        self.h = int (math.sqrt((self.base**2)+(self.altura**2)))

    def calcularArea(self):
        self.area = int((base * altura)/2)
    def calcularPerimetro(self):
        self.perimetro = int(self.base + self.altura + self.h)

class Elipse(Figura, Punto):
    def __init__(self):
        temp = Figuras_Logica.Punto()
        temp.setX(origen.getX())
        temp.setY(fin.getY())
        self.base = int(temp.calcularDistancia(fin))
        self.altura = int(temp.calcularDistancia(origen))

    def calcularArea(self):
        self.area = int((math.pi)*(self.base*self.altura))
    def calcularPerimetro(self):
        self.perimetro = int((math.pi*2)*(math.sqrt(((self.base**2)+(self.altura**2))/2)))
