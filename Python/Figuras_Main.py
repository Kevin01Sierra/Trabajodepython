import Figuras_Logica as filo


op = input ('Seleccione una figura: \n'+' 1) Cuadrado \n'+' 2) Rectangulo \n'
            +' 3) Triangulo Rectangulo \n'+' 4) Circulo \n'+' 5) Elipse \n ')

origen = filo.Punto()
fin = filo.Punto()
f = filo.Figura()

if op == 1:
    f = filo.Cuadrado()
    origen.setX(0)
    origen.setY(0)

    fin.setX(5)
    fin.setY(0)
    mostrar(f, origen, fin)
    
elif op == 2:
    f = filo.Rectangulo()
    origen.setX(0)
    origen.setY(5)

    fin.setX(10)
    fin.setY(0)
    mostrar(f, origen, fin)

elif op == 3:
    f = filo.TrianguloRectangulo()
    origen.setX(0)
    origen.setY(5)

    fin.setX(10)
    fin.setY(0)
    mostrar(f, origen, fin)

elif op == 4:
    f = filo.Circulo()
    origen.setX(0)
    origen.setY(0)

    fin.setX(5)
    fin.setY(0)
    mostrar(f, origen, fin)

elif op == 5:
    f = filo.Elipse()
    origen.setX(0)
    origen.setY(2)

    fin.setX(3)
    fin.setY(0)
    mostrar(f, origen, fin)

else:
    print('No hay más opciones.')
    
def mostrar (f, origen, fin):
    f.setOrigen(origen)
    f.setFin(fin)
    f.calcularArea()
    f.calcularPerimetro()
    print ('La area es: '+f.getArea())
    print ('El perimetro es: '+f.getPerimetro())
