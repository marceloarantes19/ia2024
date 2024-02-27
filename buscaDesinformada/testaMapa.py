from Mapa import Mapa
from Largura import Largura
l = Largura()
m = Mapa()
m.geraMapa()
origem = input("Digite a cidade de Origem: ")
destino = input("Digite a cidade de destino: ")
print(l.busca(origem, destino, m))