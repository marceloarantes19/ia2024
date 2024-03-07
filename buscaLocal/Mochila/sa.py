import random
import math
import numpy as np

def geraAgenda(t):
    x = list()
    for i in range(1,t):
        x.insert(0, i/t*10)
    x.append(0)
    print("Agenda", x)
    return x

def geraMochilaAleatoria(sAtual, n, tAgenda, iAgenda):
    l = n if iAgenda == tAgenda else 0 if n==0 else int(iAgenda/tAgenda*n)+1
    m = []
    for i in range(0, n):
        m.append(sAtual[i])
    for i in range(0, l): # Quantidade possíveis bits mutáveis
        bitAmudar = random.randrange(0,n)
        m[bitAmudar] = random.randrange(0,2)
    return m

def geraValor(p, v, m, C):
    pa = 0
    va = 0
    n = len(p)
    for i in range(0, n):
        pa = pa+p[i]*m[i]
        va = va+v[i]*m[i]
    return va if pa <= C else -1

def copiaMochila(m):
    r = list()
    for i in range(0, len(m)):
        r.append(m[i])
    return r

def sa(p, v, c, t):
    tam = t
    ag = geraAgenda(tam)
    mAtu = list()
    melhor = list()
    for i in range(0, len(p)):
        mAtu.append(0)

    mAtu = geraMochilaAleatoria(mAtu, len(mAtu), tam, tam)
    vAtu = geraValor(p, v, mAtu, c)
    melhor = copiaMochila(mAtu)
    vMelhor = vAtu

    for i in range(0, len(ag)):
        if ag[i] == 0:
            return melhor
        mNext = geraMochilaAleatoria(mAtu, len(mAtu), tam, i)
        vNext = geraValor(p, v, mNext, c)
        delta = vNext - vAtu
        if delta > 0:
            mAtu = copiaMochila(mNext)
            vAtu = vNext
            if vAtu > vMelhor:
                melhor = copiaMochila(mAtu)
                vMelhor = vAtu
        else:
            aleat = random.random()
            kk = delta/ag[i]
            x = np.exp((-1)*kk)
            x = x - int(x)
            #print(x, " - ", aleat)
            if x>aleat:
                mAtu = copiaMochila(mNext)
                vAtu = vNext
    return melhor

def cPeso(m, p):
    r = 0
    for i in range(0,len(m)):
        r = r + p[i]*m[i]
    return r

C = 12
peso  = [4, 6, 3, 2]
valor = [5, 7, 9, 6]
bm = []
bm = sa(peso, valor, C, 10)
x = []
for i in range(0, len(bm)):
    if bm[i]==1:
        x.append(i)
print(peso)
print(valor)
print(x, "Valor: ", geraValor(peso, valor, bm, C), "Peso: ", cPeso(bm, peso))
