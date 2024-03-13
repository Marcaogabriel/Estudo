Marca_de_celulares = ['Lg', 'Sansung', 'Motorola', 'Xiaomi', 'Iphone']
Valor_celular = [850, 2230, 1500, 3500, 5000]

'''
r -> Usado somente para ler algo
w -> Usado somente para escrever algo 
r+ -> Usado para ler e escrever algo
a -> Usado para acrescentar algo 
'''
#with open('valores_celulares.txt','r') as arquivo:
   # for valor in arquivo:
       # print(valor)

with open('valores_celulares.txt', 'a') as arquivo:
    for valor in Marca_de_celulares, Valor_celular:
        arquivo.write(str(valor) + '\n')