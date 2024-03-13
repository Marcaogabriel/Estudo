m = float(input('Escolha uma medida: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print(' km: \033[31m{}\033[m \n hm: \033[32m{}\033[m \n dam: \033[33m{}\033[m \n m: \033[34m{}\033[m \n dm: \033[35m{}\033[m \n cm: \033[36m{}\033[m \n mm = \033[37m{}\033[m'.format(km, hm, dam, m, dm, cm, mm))