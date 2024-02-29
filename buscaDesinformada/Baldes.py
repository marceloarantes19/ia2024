from Digrafo import Digrafo 
class Baldes(Digrafo):
  def geraBaldes(self):
    # Baldes
    vertices = []
    arestas = []
    for i in range(0,5):
      for j in range(0,4):
        estado = [i,j]
        vertices.append(estado)
    for i in vertices:
      A = i[0]
      B = i[1]
      # Encher o balde A
      if A < 4:
        estado = vertices.index([4, B])
        aresta = [i, vertices[estado]]
        arestas.append(aresta)
      # Encher o balde B
      if B < 3:
        estado = vertices.index([A, 3])
        aresta = [i, vertices[estado]]
        arestas.append(aresta)
      # Esvaziar o balde A
      if A > 0:
        estado = vertices.index([0, B])
        aresta = [i, vertices[estado]]
        arestas.append(aresta)
      # Esvaziar o balde B
      if B > 0:
        estado = vertices.index([A, 0])
        aresta = [i, vertices[estado]]
        arestas.append(aresta)
      # Passar do balde A para o balde B
      if A > 0 and B < 3:
        valorDeA  = 0 if A + B <= 3 else A - (3 - B)
        valorDeB  = 3 if A + B >= 3 else A + B
        estado = vertices.index([valorDeA, valorDeB])
        aresta = [i, vertices[estado]]
        arestas.append(aresta)
      # Passar do balde B para o balde A
      if A < 4 and B > 0:
        valorDeB  = 0 if A + B <= 4 else B - (4 - A)
        valorDeA  = 4 if A + B >= 4 else A + B
        estado = vertices.index([valorDeA, valorDeB])
        aresta = [i, vertices[estado]]
        arestas.append(aresta)
    # Retirando as duplicidades
    for i in range(0, len(arestas) - 1):
      for j in range(i+1, len(arestas)):
        if arestas[i][0] == arestas[j][0] and arestas[i][1] == arestas[j][1]:
          x = arestas.pop(j)

    for i in vertices:
      nv = "["+str(i[0])+", "+str(i[1])+"]"
      self.insereVerticeNome(nv)
    for i in arestas:
      o = "["+str(i[0][0])+", "+str(i[0][1])+"]"
      d = "["+str(i[1][0])+", "+str(i[1][1])+"]"
      self.insereArestaNome(o,d)

