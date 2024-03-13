import emoji
print('Escolha com quem o lobinho vai se casar')
print('''OPÇÕES: 
[ 1 ] Coelhinha
[ 2 ] lobinha
[ 3 ] gatinha''')
s = int(input('Faça sua escolha: '))
if s == 1:
    print(emoji.emojize('🐺 ❤ 🐇 se amam muito'))
elif s == 2:
    print('Eles não ama ela ele ama Teste de python coelhinha 🐺 💔 🐺')
elif s == 3:
    print('Ele não ama ela ele ama Teste de python coelhinha 🐺 💔 🐱')
else:
    print('Essa opção NÃO EXISTE')