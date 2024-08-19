from matplotlib import pyplot as plt

amigos = [70, 65, 72, 63, 71 , 64, 60, 64, 67]
minutos = [175, 170, 205, 120, 220, 130, 105, 145, 190]
colunas = ['a', 'b','c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(amigos,minutos)

for coluna, num_amg, num_min in zip(colunas, amigos, minutos):
    plt.annotate( coluna,
                 xy=(num_amg, num_min),
                 xytext=(5,-5),
                 textcoords='offset points')
    
plt.title("Minutos diários vs Número de amigos")
plt.ylabel("Minutos Diários Passados no Site")
plt.xlabel("numero de amigos")
plt.show()