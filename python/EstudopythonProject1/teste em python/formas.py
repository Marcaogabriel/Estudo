formadepagamento = str(input('Você está com Dinheiro? [S/N] ')).upper()[0]
        if formadepagamento == 'S':
            quanto = int(input('Quanto dinheiro você tem? '))
            outra = str(input('Esta com alguma outra forma de pagamento? [S/N] ')).upper()[0]
            if outra == 'S':
                qualoutra = int(input('''Qual a outra?
                [ 1 ] Cartão
                [ 2 ] Pix
                [ 3 ] Os Dois '''))
                qualtem = int(input('Qual destas formas você tem '))
            if outra == 'N':
                print('Pode entrar no Mercado bem vindo')
        if formadepagamento == 'N':
            outra = str(input('Esta com alguma outra forma de pagamento? [S/N] ')).upper()[0]
            if outra == 'S':
                outra = int(input('''Qual a Forma que você está?
                [ 1 ] Cartão
                [ 2 ] Pix
                [ 3 ] Os Dois '''))
            if outra == 'N':
                print('Desculpe mas Infelizmente não podera entrar no mercado')

if formadepagamento == 'N' and outra == 'N':
    break
# Dentro do Mercado