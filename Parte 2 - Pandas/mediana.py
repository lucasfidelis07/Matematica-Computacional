#Sabendo que a mediana divide um grupo de valores ao meio, 
#é possível afirmar que a Turma A e B possuem pelo menos 
#50% dos alunos acima da media 7?

import pandas as pd

vetor = [1, 3, 5, 7, 8, 1, 20, 30, 12, 32]
dados = pd.Series(vetor)
print('Mediana ', dados.median())