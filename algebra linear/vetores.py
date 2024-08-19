import re, random
from math import sqrt
from matplotlib import pyplot as plt
from collections import defaultdict, Counter

def add_vetor(v,w):
    return [v_i + w_i 
            for v_i, w_i in zip(v, w)]
    
def sub_vetor(v, w):
    return [v_pos - w_pos
            for v_pos, w_pos in zip(v,w)]
    
def somar_vetor(vetores):
    resultado = vetores[0]
    for vetor in vetores[1:]:
        resultado = add_vetor(resultado, vetor)
    return resultado

def multi_escalar(n, vetor):
    return [ n * v_pos for v_pos in vetor]

def media_vetor(vetores):
    n = len(vetores)
    return multi_escalar(1/n, somar_vetor(vetores))

def ponto(v, w):
    return sum( v_pos * w_pos for v_pos, w_pos in zip(v,w))

def soma_de_quadrados(v):
    return ponto(v, v)

def magnitude(v):
    return sqrt(soma_de_quadrados(v))

def distancia_quadrados(v, w):
    return soma_de_quadrados(sub_vetor(v,w))

def distancia(v,w):
    return sqrt(distancia(v, w))

vetor = [2, 1]
w =  [sqrt(.25), sqrt(.75)]
c = ponto(vetor,w)

vetor_em_w = multi_escalar(c,w)

zero = [0,0]

plt.arrow(0,0, vetor[0], vetor[1], width=0.002, head_width=.1)
plt.annotate("V", vetor, xytext=[vetor[0] + .1, vetor[1]])


plt.arrow(0,0, w[0], w[1], width=0.002, head_width=.1)
plt.annotate("W", w, xytext=[w[0] + .1, w[1]])

plt.annotate(u"(v * w) * w", vetor_em_w, xytext=[vetor_em_w[0] - 0.1, vetor_em_w[1] + 0.1])
plt.arrow(vetor[0], vetor[1], vetor_em_w[0] - vetor[0], vetor_em_w[1] - vetor[1], linestyle='dotted', color='blue')

plt.scatter(*zip(vetor, w, zero), marker='.')
plt.axis('equal')
plt.show()