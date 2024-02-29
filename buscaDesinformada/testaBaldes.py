from Baldes import Baldes 
from bLargura import Largura
b = Baldes()
l = Largura()
b.geraBaldes()
b.mostraGrafo()
origem = input("O estado de Origem: ")
destino = input("O estado de destino: ")
print("Largura: ", l.busca(origem, destino, b))
