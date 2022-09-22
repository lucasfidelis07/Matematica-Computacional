import matplotlib.pyplot as plt

conteudo = ['Matemática', 'História', 'Geografia']

valores = [7, 8, 6.5]

plt.bar(conteudo, valores)
plt.xlabel("Disciplinas")
plt.ylabel("Notas")
plt.show()