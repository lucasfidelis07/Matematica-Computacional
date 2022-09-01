#Crie um algoritmo para um hotel que deverá pegar quantos dias um cliente ficou hospedado.
#Para os 5 primeiros dias será dado a diária de 80 reais
#Os próximos 5 dias (do dia 6 a 10) será cobrado 60 reais
#E 50 reais para os dias que ultrapassarem o limite de 10 dias
#Exemplo (20 dias):
#5 dias (5 * 80 = 400)
#6 – 10 dias (5 * 60 = 300)
#Dia 11 a 20 (10 * 50 = 500)
#Total: 1200 reais
#Use for e if

dias = int(input('Quantos dias ficará hospedado? '))
total = 0

for i in range(0, dias):
    if (i < 5):
        total += 80
    elif(i < 10):
        total += 60
    else:
        total += 50
print('Você pagará R$' + str(total))