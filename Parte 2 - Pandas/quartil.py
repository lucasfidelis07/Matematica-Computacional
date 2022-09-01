#Qual turma possui o pior rendimento entre os 25% piores alunos (Q1)?

import pandas as pd

vetor = [1, 3, 5, 7, 8, 1, 20, 30, 12, 32]
dados = pd.Series(vetor)
print('Quartil: ', dados.quantile())