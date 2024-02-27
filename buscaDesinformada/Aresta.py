from Vertice import Vertice
class Aresta:
  # Tipo 1 = Grafo. Tipo 2 = Dígrafo
  def __init__(self, origem = None, destino = None, valor = 0):
    self.__origem = origem
    self.__destino = destino
    self.__valor = valor
  def getOrigem(self):
    return self.__origem
  def setOrigem(self, origem):
    self.__origem = origem
  def getDestino(self):
    return self.__destino
  def setDestino(self, destino):
    self.__destino = destino
  def getValor(self):
    return self.__valor
  def setValor(self, valor):
    self.__valor = valor

