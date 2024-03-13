def escrever(msg):
    qnt = len(msg)
    print('-=' * qnt)
    print(f'    {msg}')
    print('-=' * qnt)


escrever(input('Escreva algo: '))