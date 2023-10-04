from my_libraries.coordsystems import Ponto, Reta, Circulo, Retangulo

def workspace():
    pt = Ponto(1,2)
    pt.mostrar_coordenadas()

    rt = Reta(0,-2,2,-4)
    rt.distancia_ponto_reta(1,2)
    rt.verifica_ponto_reta(1,-3)

    cl = Circulo(0,0,5)
    cl.calcula_area()
    cl.calcula_comprimento()
    cl.verifica_ponto_circulo(1,2)

    ret = Retangulo(3,4)
    ret.retangle_area()
    ret.retangle_diagonal()

if __name__ == "__main__":
    workspace()
