from matplotlib import pyplot as plt
from collections import Counter

notas = [83, 93, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
aproximacao = lambda nota: nota // 10 * 10
histograma = Counter(aproximacao(nota) for nota in notas)

plt.bar([x for x in histograma.keys()],
        histograma.values(),
        8)

plt.axis([-5, 105, 0, 5])

plt.xticks([10 * i for i in range(11)])
plt.ylabel("# de Alunos")
plt.xlabel("Proximidade")
plt.title("Distribuição de notas do teste 1")
plt.show()
