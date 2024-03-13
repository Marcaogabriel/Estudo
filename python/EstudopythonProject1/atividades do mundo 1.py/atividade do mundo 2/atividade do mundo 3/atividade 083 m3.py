e = str(input('Digite sua experssão: '))
p = []
for s in e:
    if s == '(':
        p.append('(')
    elif s == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(')')
            break
if len(p) == 0:
    print('Sua expressão está correta')
else:
    print('Sua expressão está incorreta')