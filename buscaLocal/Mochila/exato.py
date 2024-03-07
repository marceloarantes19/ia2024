def divEConq(m, a, p, v, n, C):
    if a == n:
        return m
    else:
        k = []
        l = []
        a = a+1
        for i in m:
            k.append(i)
            l.append(i)
        l.append(a)
        nk = []
        nl = []
        nk = divEConq(k, a, p, v, n, C)
        nl = divEConq(l, a, p, v, n, C)
        return nk if cValor(nk, v, p, C) > cValor(nl, v, p, C) else nl

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
#divEConq([], -1, peso, valor, len(peso)-1, C)
#bm = []
bm = divEConq([], -1, peso, valor, len(peso)-1, C)
print("\n\nMochila", bm, "Valor: ", cValor(bm, valor, peso, C), "Peso: ", cPeso(bm, peso))
