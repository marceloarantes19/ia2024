from Mapa import Mapa
from bLargura import Largura
from bProfundidade import Profundidade
from bAprofundamento import AprofundamentoInterativo
l = Largura()
p = Profundidade()
a = AprofundamentoInterativo()
m = Mapa()
m.geraMapa()
origem = input("Digite a cidade de Origem: ")
destino = input("Digite a cidade de destino: ")
#print("Largura: ", l.busca(origem, destino, m))
#print("Profundidade: ", p.busca(origem, destino, m))
print("Aprofundamento: ", a.busca(origem, destino, m))