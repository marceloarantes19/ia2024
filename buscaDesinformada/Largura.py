class Largura:
  def mostraCaminho(self, f, p, a):
    if a == 0:
      return f[0].getNome()
    else:
      return self.mostraCaminho(f, p, p[a]) + " - " + f[a].getNome()

  def busca(self, origem, destino, g): # Nome dos vértices
    o = g.getVerticeNome(origem)
    d = g.getVerticeNome(destino)
    if g.verticeExiste(o) and g.verticeExiste(d):
      fila = []
      pai = []
      inicio = -1
      fim = 0
      fila.append(o)
      pai.append(-1)
      while len(fila) > inicio:
        inicio = inicio + 1
        atual = fila[inicio]
        if atual == d:
          return self.mostraCaminho(fila, pai, inicio)
        for i in g.getSucessor(atual):
          fila.append(i)
          pai.append(inicio)
    return "Caminho não encontrado!"

