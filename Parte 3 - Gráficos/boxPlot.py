import matplotlib.pyplot as plt

v1 = [1, 2, 3, 6, 6, 8, 9, 12, 22]
v2 = [8, 12, 15, 28, 12, 30]
plt.boxplot([v1, v2], labels=["Exemplo 1", "Exemplo 2"])
plt.show()
