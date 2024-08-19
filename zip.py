lista1= ['a','b','c']
lista2= [1,2,3]
listas_compscatadas = list(zip(lista1, lista2))

print(listas_compscatadas)

def magic_way(x,y,z):
    return x+y+z

lista_xy = [1,2]
z_dicionario = {"z": 3}

print(magic_way(*lista_xy, **z_dicionario))