a = input('Digite algo: ')
print('\033[31mOque ele é?\033[m', type(a))
print('\033[32mé alfanumerico?\033[m ', a.isalnum())
print('\033[33mé número?\033[m ', a.isnumeric())
print('\033[34mé Letra?\033[m', a.isalpha())
print('\033[35mé Minisculo?\033[m ', a.islower())
print('\033[36mé Maiusculo?\033[m ', a.isupper())