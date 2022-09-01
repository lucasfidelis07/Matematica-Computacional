#SABENDO QUE UMA ESCOLA POSSUÍA AS TURMAS A E B, 
#QUAL DAS TURMAS POSSUI MELHOR RENDIMENTO?

import pandas as pd

turmaA = [8, 2, 7, 9, 10, 4.5, 7, 8, 9.5, 7.5, 2, 7, 7]
turmaB = [2, 6, 7, 10, 9.5, 7.5, 3, 10, 8, 9, 8, 2, 10]

dadosA = pd.Series(turmaA)
print('Média ', dadosA.mean())

dadosB = pd.Series(turmaB)
print('Média ', dadosB.mean())