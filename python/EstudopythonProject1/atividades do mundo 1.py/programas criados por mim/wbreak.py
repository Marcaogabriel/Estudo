a = s = c = 0
while True:
    a = int(input('Digite um número: '))
    if a == 999:
        break
    s += a
    c += 1
print(f'Você digitou {c} e a soma deles é = {s}')