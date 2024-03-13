import pyautogui
import time
pyautogui.PAUSE = 0.7
while True:
    print('''O que Você deseja?
       [ 1 ] Abrir Meu jogo de xadrez
       [ 2 ] Baixar uma imagem
       [ 3 ] Pesquisar um video para assistir
       [ 4 ] Saber posição
       [ 0 ] Sair do programa''')
    e = int(input('Escolha uma opção: '))
    # oq acontece com cada opção
    if e == 1:
        pyautogui.alert('O PROGRAMA VAI COMEÇAR NÃO TOQUE NO MOUSE NEM NO TECLADO')
        pyautogui.press('win')
        pyautogui.write('chrome')
        pyautogui.press('enter')
        time.sleep(4.2)
        pyautogui.click(754, 382)
        time.sleep(3)
        pyautogui.write('https://www.chess.com/home')
        pyautogui.press('enter')
        pyautogui.alert('O PROGRAMA ACABOU PODE USAR O TECLADO E MOUSE')
    elif e == 2:
        a = str(input('Escolha o que você quer pesquisar: '))
        pyautogui.alert('O PROGRAMA VAI COMEÇAR NÃO TOQUE NO MOUSE NEM NO TECLADO')
        pyautogui.press('win')
        pyautogui.write('chrome')
        pyautogui.press('enter')
        time.sleep(1.3)
        pyautogui.click(754, 382)
        time.sleep(1.5)
        pyautogui.click(498, 456)
        pyautogui.write(a)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(271, 153)
        time.sleep(2)
        pyautogui.click(319, 321)
        time.sleep(1)
        pyautogui.click(1022, 225, button = 'right')
        time.sleep(1)
        pyautogui.click(1030, 517)
        time.sleep(1.5)
        pyautogui.press('enter')
        pyautogui.alert('O PROGRAMA ACABOU PODE USAR O TECLADO E MOUSE')
    elif e == 3:
        y = str(input('Escolha oque você quer pesquisar'))
        pyautogui.alert('O PROGRAMA VAI COMEÇAR NÃO TOQUE NO MOUSE NEM NO TECLADO')
        pyautogui.press('win')
        pyautogui.write('chrome')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(754, 382)
        time.sleep(1.5)
        pyautogui.write('youtube')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.alert('O PROGRAMA ACABOU PODE USAR O TECLADO E MOUSE')
    elif e == 4:
        v = pyautogui.position()
        time.sleep(2)
        print(v)

    elif e == 0:
        break

    else:
        print('Opção Invalida! tente novamente')
