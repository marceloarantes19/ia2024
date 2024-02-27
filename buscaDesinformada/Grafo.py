from Vertice import Vertice
from Aresta import Aresta
class Grafo:
  def __init__(self):
    self.__vertices = []
    self.__arestas = []
  def getVertices(self):
    return self.__vertices
  def getVerticeNome(self, n):
    for i in self.getVertices():
      if i.getNome() == n:
        return i
    return None
  def setVertices(self, vertices):
    self.__vertices = vertices
  def getArestas(self):
    return self.__arestas
  def setArestas(self, arestas):
    self.__arestas = arestas 
  def verticeExiste(self, v):
    return v in self.__vertices
  def verticeExisteNome(self, n):
    for v in self.getVertices():
      if n == v.getNome():
        return True 
    return False
  
  def insereVertice(self, v): # Recebe um Vértice
    if not self.verticeExiste(v):
      self.getVertices().append(v)

  def insereVerticeNome(self, n):
    if not self.verticeExisteNome(n):
      v = Vertice(n)
      self.__vertices.append(v)

  def arestaExiste(self, o, d):
    for i in self.__arestas:
      if o == i.getOrigem() and d == i.getDestino():
        return True
    return False

  def insereAresta(self, o, d, vl = 0): # Recebe dois Vértices e o valor
    if not self.arestaExiste(o, d):
      a = Aresta(o, d, vl)
      b = Aresta(d, o, vl)
      self.getArestas().append(a)
      self.getArestas().append(b)
  
  def insereArestaNome(self, o, d, vl = 0):
    vo = self.getVerticeNome(o)
    vd = self.getVerticeNome(d)
    if vo != None and vd != None:
      self.insereAresta(vo, vd, vl)

  def getSucessor(self, v):
    ret = []
    for i in self.getArestas():
      if v == i.getOrigem():
        ret.append(i.getDestino())
    return ret
  