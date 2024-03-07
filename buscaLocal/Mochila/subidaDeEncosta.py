import random

def hillClimb(p, v, C):
    n = len(p)
    vAtual = -1
    while vAtual == -1:
        mAtual = []
        sAtual = random.randrange(0, n)
        mAtual = geraMochila(sAtual, n)
        #mAtual = [0, 0, 1, 0, 0, 1, 0]
        vAtual = geraValor(p, v, mAtual, C)
    while True:
        print("Mochila Atual: ", mAtual)
        mPrx, vPrx = melhorVizinho(p, v, mAtual, C)
        #vPrx = geraValor(p, v, mPrx, C)
        if vPrx > vAtual:
            mAtual = []
            vAtual = vPrx
            for i in range(0, n):
                mAtual.append(mPrx[i])
        else:
            print("Mochila Atual: ", mAtual)
            return mAtual

def geraMochila(sAtual, n):
    l = 0
    m = []
    v = sAtual
    while v > 0:
        m.insert(0, v%2)
        v = v//2
        l = l + 1
    while l < n:
        m.append(0)
        l = l + 1
    return m

def geraValor(p, v, m, C):
    pa = 0
    va = 0
    n = len(p)
    for i in range(0, n):
        pa = pa+p[i]*m[i]
        va = va+v[i]*m[i]
    return va if pa <= C else -1

def melhorVizinho(p, v, m, C):
    n = len(p)
    novaMochila = []
    melhorMochila = []
    valorDaMochila = geraValor(p, v, m, C)
    for j in range(0, n):
        melhorMochila.append(m[j])
    valorDaMM = valorDaMochila
    for i in range(0, n):
        novaMochila = []
        for j in range(0, n):
            novaMochila.append(m[j])
        novaMochila[i] = 0 if m[i]==1 else 1
        novoValor = geraValor(p,v,novaMochila,C)
        if novoValor > valorDaMM:
            valorDaMM = novoValor
            melhorMochila = []
            for j in range(0, n):
                melhorMochila.append(novaMochila[j])
    return melhorMochila, valorDaMM

def cPeso(m, p):
    r = 0
    for i in range(0,len(m)):
        r = r + p[i]*m[i]
    return r

C = 12
peso  = [4, 6, 3, 2]
valor = [5, 7, 9, 6]
bm = []
bm = hillClimb(peso, valor, C)
x = []
for i in range(0, len(bm)):
    if bm[i]==1:
        x.append(i)
print(peso)
print(valor)
print(x, "Valor: ", geraValor(peso, valor, bm, C), "Peso: ", cPeso(bm, peso))
