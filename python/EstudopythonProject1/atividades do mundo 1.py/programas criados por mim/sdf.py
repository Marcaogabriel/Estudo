import schedule
import time

def tafera_importante():
    print('fazendo dinheiro...')

#schedule cada tempo para fazer ex: segunda, terça etc
schedule.every(5).seconds.do(tafera_importante)
while 1:
    schedule.run_pending()
    time.sleep(3)