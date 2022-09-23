import matplotlib.pyplot as plt

conteudo = ["Matemática", "História", "Geografia"]
valores = [7, 8, 6.5]
plt.pie(valores, labels=conteudo, autopct="%.2f%%")
plt.title("Média de notas")
plt.show()