import math
an = float(input('Digite o angulo você deseja: '))
seno = math.sin(math.radians(an))
print('o ângulo de \033[31m{}\033[m tem o SENO de \033[32m{:.2f}\033[m'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('o ângulo de \033[33m{}\033[m tem o COSSENO de \033[34m{:.2f}\033[m'.format(an, cosseno))
tangente = math.tan(math.radians(an))
print('o ângulo de \033[35m{}\033[m tem o TANGENTE de \033[36m{:.2f}\033[m'.format(an, tangente))
