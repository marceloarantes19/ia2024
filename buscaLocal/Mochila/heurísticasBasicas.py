def firstFit(m, p, C):
    pR = 0
    for i in range(0, len(p)):
        if p[i]+pR <= C:
            m.append(i)
            pR = pR + p[i]
    return m

def bestFit(m, p, v, C):
    pR = 0
    ad = True
    n = len(p)
    inserido = []

    while ad:
        ia = -1
        ad = False
        for i in range(0, n):
            if not (i in m) and pR + p[i]<= C and (ia == -1 or p[i]<p[ia]):
                ia = i
        if ia >= 0:
            pR = pR + p[ia]
            m.append(ia)
            ad = True
    return m

def worstFit(m, p, v, C):
    pR = 0
    ad = True
    inserido = []

    while len(p) > 0 and ad:
        ia = -1
        ad = False
        for i in range(0, len(p)):
            if not (i in m) and pR + p[i]<= C and (ia == -1 or p[i]<p[ia]):
                ia = i
        if ia >= 0:
            pR = pR + p[ia]
            m.append(ia)
            ad = True
    return m


def cValor(m, v, p, C):
    r = 0
    for i in m:
        r = r + v[i]
    return r if cPeso(m, p)<= C else r*(-1)

def cPeso(m, p):
    r = 0
    for i in m:
        r = r + p[i]
    return r

C = 12
peso  = [4, 6, 3, 2]
valor = [5, 7, 9, 6]
#peso  = [4, 6, 3, 2, 9, 1, 7]
#valor = [5, 7, 9, 6, 20, 5, 4]

bm = []
bm = bestFit([], peso, valor, C)

#bm = firstFit([], peso, C)
print(bm, "Valor: ", cValor(bm, valor, peso, C), "Peso: ", cPeso(bm, peso))
