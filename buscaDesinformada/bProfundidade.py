class Profundidade:
  def mostraCaminho(self, f, p, a):
    if a == 0:
      return f[0].getNome()
    else:
      return self.mostraCaminho(f, p, p[a]) + " - " + f[a].getNome()

  def busca(self, origem, destino, g): # Nome dos vértices
    o = g.getVerticeNome(origem)
    d = g.getVerticeNome(destino)
    if g.verticeExiste(o) and g.verticeExiste(d):
      pilha = []
      pai = []
      fim = 0
      visitado = []
      pilha.append(o)
      pai.append(-1)
      while len(pilha) > 0:
        atual = pilha[fim] 
        indAtu = fim
        print(atual.getNome())
        if atual == d:
          return self.mostraCaminho(pilha, pai, indAtu)
        elif atual.getEstado() == 0 and atual not in visitado:
          for i in g.getSucessor(atual):
            pilha.append(i)
            pai.append(indAtu)
            fim = fim + 1
          atual.setEstado(1)
          visitado.append(atual)
        elif atual.getEstado() == 1:
          ret = pilha.pop()
          retP = pai.pop()
          print("Sai da Memória: ", ret.getNome())
          fim = fim - 1
    return "Caminho não encontrado!"

