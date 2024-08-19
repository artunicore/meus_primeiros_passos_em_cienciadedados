from matplotlib import pyplot as plt

variancia = [1, 2, 4, 8, 16, 32, 64, 128, 256]
polarizacao_ao_quadrado = [256 ,128,64, 32, 16, 8, 4, 2, 1]
erro_total = [x + y for x,y in zip(variancia, polarizacao_ao_quadrado) ]

xs = [i for i, _ in enumerate(variancia)]

plt.plot(xs, variancia, 'g-', label='Variância')
plt.plot(xs, polarizacao_ao_quadrado, 'r.', label='Polarização^2')
plt.plot(xs, erro_total, 'r:', label='Erro Total')

plt.legend(loc=9)
plt.xlabel("Complexidade do modelo")
plt.title("Compromisso entre polarização e Variância")
plt.show()