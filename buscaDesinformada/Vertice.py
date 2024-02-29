class Vertice:
  def __init__(self, n = None):
    self.__nome = n 
    self.__estado = 0 # 0 - aberto (não visitado) - 1 - Visitado
  def getNome(self):
    return self.__nome 
  def setNome(self, n):
    self.__nome = n
  def getEstado(self):
    return self.__estado
  def setEstado(self, e): 
    self.__estado = e
    