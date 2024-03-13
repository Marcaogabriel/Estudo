dinheirototal = int(input('Digite o seu saldo total: '))
carteira = 0
print('-=' * 30)
print('BEM VINDO AO CAIXA ELETRÔNICO')
print('-=' * 30)
while True:
    print(''' O que deseja fazer?2
    [ 1 ] Saque
    [ 2 ] Deposito
    [ 3 ] Transferencia
    [ 4 ] Pix
    [ 0 ] Sair''')
    escolha = int(input('Oque deseja fazer? '))
    if escolha == 1:
        sacar = int(input('Quanto você deseja sacar? '))
        dinheirototal - sacar
        carteira + sacar

        print(f'Você tem {carteira}R$ na carteira e ficou com o saldo total de {dinheirototal}')
    elif escolha == 2:
        if carteira <= 0:
            print('Você não pode depositar nada sem dinheiro saque algo primeiro')
        elif carteira >= 1:
            depositar = int(input('Quanto você deseja depositar? '))
            if depositar > carteira:
                print('Você não pode depositar mais do que você tem')
            elif depositar < 0:
                print('Você não pode depositar número negativo')
            elif depositar == 0:
                print(f'Você depositou {depositar} reais logo não vai mudar nada')
            else:
                carteira - depositar
                dinheirototal + depositar
                print(f'Você ficou com {carteira}R$ na carteira e depositou {depositar}R$ e ficou com {dinheirototal}R$ no banco')
    elif escolha == 3:
        transferencia = int(input('Quanto você quer transferir? '))
        if transferencia > dinheirototal:
            pergunta = ' '
            while pergunta not in 'SN':
                pergunta = str(input('Seu saldo ficara negativo tem certeza que quer continuar a transferência? [S/N]'))
                if pergunta == 'N':
                    break
                else:
                    while True:
                        qualdestino = int(input('Digite o número da conta da pessoa (7 números): '))
                        if len(qualdestino) != 7:
                            print('Conta Invalida reescreva a conta do destinatario')
                        else:
                            dinheirototal - transferencia
                            print(f'A sua transferencia foi feita para a conta {qualdestino} no valor de {transferencia} você ficou com o saldo de {dinheirototal}')
                            break
        else:
            while True:
                qualdestino = int(input('Digite o número da conta da pessoa (7 números): '))
                if len(qualdestino) != 7:
                    print('Conta Invalida reescreva a conta do destinatario')
                else:
                    dinheirototal - transferencia
                    print(f'A sua transferencia foi feita para a conta {qualdestino} no valor de {transferencia} você ficou com o saldo de {dinheirototal}')
                    break
    #elif escolha == 4:

    elif escolha == 0:
        break
        print('Foi bom vê-lo no banco até a próxima')
    else:
        print('Opção, Invalida tente novamente')