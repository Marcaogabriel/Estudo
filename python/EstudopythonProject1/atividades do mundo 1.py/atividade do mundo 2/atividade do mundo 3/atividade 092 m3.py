from datetime import date
ano = date.today().year
dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['idade'] = int(input('Ano de nascimento: '))
dados['Carteira de Trabalho'] = int(input('Carteira de trabalho: (0 se não tiver) '))
idade = ano - dados['idade']
if dados['Carteira de Trabalho'] != 0:
    dados['Ano de contrato'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário:  R$'))
    aposentado = dados['Ano de contrato'] - dados['idade']
    apose = aposentado + 35
    dados['idade'] = idade
    for v, i in dados.items():
        print(f'   => {v} tem o valor {i}')
    print(f'   => E {dados["Nome"]} sera aposentado com {apose} anos')

else:
    print(f'   => {dados["Nome"]} tem {idade} anos e não trabalha')
