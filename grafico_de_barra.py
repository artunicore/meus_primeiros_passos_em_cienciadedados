from matplotlib import pyplot as plt

jogos = ['megaman zero', 'bufos', 'despertar da floresta', 'kof 2002']
minhas_notas = [2, 10 , 9, 3]

xs = [ i + 0.1 for i, _ in enumerate(jogos)]

plt.bar(xs, minhas_notas)

plt.ylabel("notas do arcunimorte")

plt.title("Meus jogos favoritos")

plt.xticks([i + 0.5 for i, _ in enumerate(jogos)],jogos)

plt.show()
