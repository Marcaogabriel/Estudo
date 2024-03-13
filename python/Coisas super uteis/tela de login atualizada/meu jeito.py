import PySimpleGUI as sg

sg.theme('Dark Green 3')
BAR_MAX = 1000
# Layout das telas
def tela_inicial():
    layout = [
        [sg.Text('Usuário')],
        [sg.Input(key='usuario')],
        [sg.Text('Senha')],
        [sg.Input(key='senha')],
        [sg.Button('login'), sg.Button('Cadastrar novo usuário')],
        [sg.Text('',key='mensagem')]
    ]
    return sg.Window('Login',layout=layout, finalize=True)


def tela_de_cadastramento():
    layout = [
        [sg.Text('Usuário')],
        [sg.Input(key='usuario1')],
        [sg.Text('Senha')],
        [sg.Input(key='senha1')],
        [sg.Button('Cadastrar')],
        [sg.Text('',key='mensagem')]
    ]
    return sg.Window('Login',layout=layout, finalize=True)



def tela_de_cadastramento_de_produtos():
    layout = [
        #[sg.ProgressBar(BAR_MAX, orientation='h', size=(50, 150), key='Tela') sg.Text('',key='mensagem1')],
        [sg.Text('Produto'), sg.Input(key='Produto', size=(13, 10))],
        [sg.Text('Quantidade'), sg.Input(key='Quantidade', size=(10, 10))],
        [sg.Text('Preço'), sg.Input(key='Preço', size=(15, 10))],
        [sg.Button('Cadastramento'), sg.Button('Voltar')],
        [sg.Text('', key='mensagem1')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)


# Criar as janelas
janela1, janela2, janela3 = tela_inicial(), None, None

# Criar uns loop de leitura de eventos
while True:
    window,event,values = sg.read_all_windows()
    # Quando a janela fechar
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    # Quando querer ir para a próxima janela
    if window == janela1 and event == 'Cadastrar novo usuário':
        janela2 = tela_de_cadastramento()
        janela1.hide()

    # Quando querer voltar para a janela
    if window == janela2 and event == 'Cadastrar':
        if event == 'Cadastrar':
            usuario = values['usuario1']
            senha = values['senha1']


        janela2.hide()
        janela1.un_hide()

    # Oque deve acontecer quando clicar no botão login
    if window == janela1 and event == 'login':
        if values['usuario'] == usuario and values['senha'] == senha:
            janela1.hide()
            janela3 = tela_de_cadastramento_de_produtos()

    # Caso erre o login ou a senha
        else:
            window['mensagem'].update('Senha ou usuario incorreto')

    # Cadastrar um Produto (Beta)
    if window == janela3 and event == 'Cadastramento':
        Produto = values['Produto']
        Quantidades = int(values['Quantidade'])
        Preço = float(values['Preço'])
        window['mensagem1'].update(f'O produto {Produto} está com aproximadamente {Quantidades} itens no estoque e está no preço de     R${Preço}')

    #Voltar para a janela 1
    if window == janela3 and event == 'Voltar':
        janela3.hide()
        janela1.un_hide()


