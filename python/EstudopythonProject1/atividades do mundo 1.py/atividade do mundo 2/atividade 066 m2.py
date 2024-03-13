numero = soma = contagem = 0

while True:
    numero = int(input('Digite um número [999 para parada]: '))
    if numero == 999:
        break
    else:
        soma += numero
        contagem += 1
print(f'O total de números digitados foi {contagem} e a soma entre eles foi {soma}')