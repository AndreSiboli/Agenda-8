rates = []

for i in range(1, 51):
    name = input('Qual é o seu nome? ')
    age = input('Qual a sua idade? ')

    print('Avaliação do atendimento.\n')
    print('1 - Excelente')
    print('2 - Bom')
    print('3 - Ruim\n')

    rate = int(input('Digite 1, 2 ou 3 para avaliar: '))

    if rate in [1, 2, 3]:
        rates.append({'name': name, 'age': age, 'rate': rate})
        print('Agradecemos sua avaliação.\n')
    else:
        print('Número inválido.\n')

excelent = 0
good = 0
bad = 0

for i in range(0, len(rates)):
    if rates[i]['rate'] == 1:
        excelent += 1
    elif rates[i]['rate'] == 2:
        good += 1
    elif rates[i]['rate'] == 3:
        bad += 1

print("\n=== RESULTADO DA PESQUISA ===")
print(f"Quantidade de respostas EXCELENTE: {excelent}")
print(f"Quantidade de respostas BOM: {good}")
print(f"Quantidade de respostas RUIM: {bad}")