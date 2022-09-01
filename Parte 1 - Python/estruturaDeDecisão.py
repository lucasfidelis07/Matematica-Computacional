#Pergunte ao usuário a sua média e informe:
#“Aprovado” caso nota maior que 7
#“Recuperação” se média estiver abaixo de 7, mas acima de 4
#“Reprovado” caso média esteja abaixo de 4.

media = float(input('Media: '))
if (media > 7):
    print('Aprovado')
elif (media > 4):
    print('Recuperação')
else:
    print('Reprovado')