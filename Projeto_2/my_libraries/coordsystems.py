class Ponto():
    def __init__(self,x,y):
        self._x = x
        self._y = y
    
    def mostrar_coordenadas(self):
        print(f'\nO seu ponto possui as coordenadas: ({self._x},{self._y}).\n')

class Reta(Ponto):
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.m = (self.y2 - self.y1)/(self.x2 - self.x1)
        self.n = self.y1 - self.m*self.x1
        if self.n > 0:
            self.equacao_reta = f'y = {self.m}*x + {self.n}'
        elif self.n == 0:
            self.equacao_reta = f'y = {self.m}*x'
        else:
            self.equacao_reta = f'y = {self.m}*x {self.n}'
        print(f'\nA equação da reta gerada pelos dois pontos é: {self.equacao_reta}\n')
    
    def distancia_ponto_reta(self,x,y):
        super().__init__(x,y)
        cima = (-self.m*self._x + self._y - self.n)**(1/2)
        baixo = (self.m**2 + 1)**(1/2)
        distancia = cima/baixo
        print(f'\nA distância entre a reta e o ponto ({self._x},{self._y}) é: {distancia}\n')
    
    def verifica_ponto_reta(self,x,y):
        super().__init__(x,y)
        y1 = self.m*self._x + self.n
        if y1 == self._y:
            print(f'\nO ponto ({self._x},{self._y}) está contido na reta!\n')
        else:
            print(f'\nO ponto ({self._x},{self._y}) não está contido na reta!\n')

class Circulo(Ponto):
    def __init__(self,x1,y1,raio):
        self.centroX = x1
        self.centroY = y1
        self.raio = raio
        if self.centroX > 0:
            if self.centroY > 0:
                print(f'\nA equação do círculo é: (x - {self.centroX})^2 + (y - {self.centroY})^2 = {self.raio}^2\n')
            elif self.centroY == 0:
                print(f'\nA equação do círculo é: (x - {self.centroX})^2 + y^2 = {self.raio}^2\n')
            else:
                print(f'\nA equação do círculo é: (x - {self.centroX})^2 + (y {self.centroY})^2 = {self.raio}^2\n')
        elif self.centroX == 0:
            if self.centroY > 0:
                print(f'\nA equação do círculo é: x^2 + (y - {self.centroY})^2 = {self.raio}^2\n')
            elif self.centroY == 0:
                print(f'\nA equação do círculo é: x^2 + y^2 = {self.raio}^2\n')
            else:
                print(f'\nA equação do círculo é: x^2 + (y {self.centroY})^2 = {self.raio}^2\n')
        else:
            if self.centroY > 0:
                print(f'\nA equação do círculo é: (x {self.centroX})^2 + (y - {self.centroY})^2 = {self.raio}^2\n')
            elif self.centroY == 0:
                print(f'\nA equação do círculo é: (x {self.centroX})^2 + y^2 = {self.raio}^2\n')
            else:
                print(f'\nA equação do círculo é: (x {self.centroX})^2 + (y {self.centroY})^2 = {self.raio}^2\n')
            
    def calcula_area(self):
        area = 3.14*(self.raio**2)
        print(f'\n A área do círculo é: {area}\n')
    
    def calcula_comprimento(self):
        comprimento = 2*3.14*self.raio
        print(f'\nO comprimento do círculo é: {comprimento}\n')

    def verifica_ponto_circulo(self,x,y):
        super().__init__(x,y)
        soma_quadrados = (self._x - self.centroX)**2 + (self._y - self.centroY)**2
        distancia = soma_quadrados**(1/2)
        if distancia > self.raio:
            print(f'\nO ponto ({self._x},{self._y}) não pertence ao círculo\n')
        else:
            print(f'\nO ponto ({self._x},{self._y}) pertence ao círculo\n')
        
class Retangulo():
    def __init__(self,largura,comprimento):
        self.largura = largura
        self.comprimento = comprimento

    def retangle_area(self):
        area = self.largura * self.comprimento
        print(f'\nA área do retângulo é {area}\n')
    
    def retangle_diagonal(self):
        soma_quadrados = self.largura**2 + self.comprimento**2
        diagonal = soma_quadrados**(1/2)
        print(f'\nA diagonal do retângulo tem comprimento de {diagonal}\n')