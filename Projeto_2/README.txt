Foi criado neste projeto uma pasta chamada "my_libraries" na qual ficará as bibliotecas com as classes que vou importar
no arquivo principal do meu projeto, que é o "testbench_1.0.py"

Dentro de my_libraries tem:
- Arquivo "__init__.py": para o sistema entender que ali é onde ficará a biblioteca e as classes
- Arquivo "coordsystems.py": para criar as classes que irei utilizar em "testebench_1.0.py"
    Neste arquivo, temos as classes Ponto, Reta, Circulo e Retangulo.
        - Classe Ponto: vou armazenar os dados das coordenadas do ponto e direi ao usuário elas
        - Classe Reta: através de 2 pontos, direi a equação da reta, calculo a distância entre um ponto e a reta já criada
          anteriormente e se um ponto está contido nessa mesma reta
        - Classe Circulo: pegarei as coordenadas do centro do circulo, pegarei o raio do circulo e direi a equação do
          circulo, além de calcular a área e comprimento do mesmo e dizer se um ponto está contido nesse círculo
        - Classe Retangulo: pegarei a largura e comprimento do retangulo e direi sua área e sua diagonal

No arquivo principal "testbench_1.0.py"
- Importarei as classes do arquivo "coordsystems.py"
- Colocarei uns exemplos testando as funções das classes.