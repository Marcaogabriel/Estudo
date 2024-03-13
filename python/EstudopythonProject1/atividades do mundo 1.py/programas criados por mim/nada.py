import pyautogui
import time

e = ''
while True:
    print('Deseja falar eu te amo para kamila?')
    e = str(input('Faça sua Escolha: [S/N] ')).upper()[0]
    if e == 'S':
        a = str(input('Escolha Teste de python frase que você deseja mandar para ela: '))
        pyautogui.PAUSE = 1
        print('Espere 2 segundos...')
        time.sleep(2)
        pyautogui.click(x=903, y=738)
        pyautogui.click(x=153, y=306)
        pyautogui.write(a)
        pyautogui.press('Enter')
    elif e == 'N':
        break
    else:
        print('Opção Invalida tente novamente')
    time.sleep(2)