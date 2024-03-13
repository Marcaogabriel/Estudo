frase = str(input('Digite uma frase: ')).strip().upper() #strip = eliminar espaços
palavras = frase.split() # Dividir as palavras           #upper = deixar tudo maiusculo
juntar = ''.join(palavras)  #Vai juntar as palavras
inverso = ''
for letra in range(len(juntar) -1, -1, -1):  #len -1 = pega o números de letras da variavel elimina Teste de python ultima letra  b-1 =vai ate antes da primeira p-1 = vai voltando
    inverso += juntar[letra]
print('O inverso de {} é {}'.format(juntar, inverso))
if inverso == juntar:
    print('Temos um palíndromo')
else:
    print('A frase dita não é um palíndromo')