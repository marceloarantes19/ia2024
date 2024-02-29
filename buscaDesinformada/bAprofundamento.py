class AprofundamentoInterativo:
  def mostraCaminho(self, f, p, a):
    if a == 0:
      return f[0].getNome()
    else:
      return self.mostraCaminho(f, p, p[a]) + " - " + f[a].getNome()

  def busca(self, origem, destino, g): # Nome dos vértices
    o = g.getVerticeNome(origem)
    d = g.getVerticeNome(destino)
    if g.verticeExiste(o) and g.verticeExiste(d):
      l = -1
      while True:
        l = l + 1 # limite da busca
        # Joga a Busca fora
        print("Nivel:", l)
        # zera estados do vértices
        g.zeraEstadoVertices()
        pilha = list()
        pai = list()
        prof = list()
        fim = 0
        visitado = list()
        pilha.append(o)
        pai.append(-1)
        prof.append(0)
        while len(pilha) > 0:
          atual = pilha[fim] 
          pAtual = prof[fim]
          indAtu = fim
          print(atual.getNome(), atual.getEstado(), pAtual)
          if atual == d:
            return self.mostraCaminho(pilha, pai, indAtu)
          elif pAtual < l and atual.getEstado() == 0 and atual not in visitado:
            for i in g.getSucessor(atual):
              pilha.append(i)
              pai.append(indAtu)
              prof.append(pAtual + 1)
              fim = fim + 1
            atual.setEstado(1)
            visitado.append(atual)
          elif atual.getEstado() == 1 or pAtual >= l:
            pilha.pop()
            pai.pop()
            prof.pop()
            fim = fim - 1
    return "Caminho não encontrado!"

