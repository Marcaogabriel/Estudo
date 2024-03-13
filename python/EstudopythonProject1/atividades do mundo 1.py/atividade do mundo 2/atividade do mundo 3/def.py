
def l(txt):
    print('-=' * 20)
    print(txt)
    print('-=' * 20)


n = int(input('Quantos nomes você quer digitar: '))

for p in range(0, n):
    l(str(input('Digite algo: ')))



