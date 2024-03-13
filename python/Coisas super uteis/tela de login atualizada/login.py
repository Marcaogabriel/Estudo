import PySimpleGUI as sg

layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')], [sg.Button('Cadastrar novo usuario')],
    [sg.Text('',key='mensagem')]
]

window = sg.Window('Login',layout=layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        senha_correta = '1234'
        usuario_correto = 'marcos'
        usuario = values['usuario']
        senha = values['senha']

        if senha == senha_correta and usuario == usuario_correto:
            window['mensagem'].update('Login feito com sucesso')

        else:
            window['mensagem'].update('Senha ou usuario incorreto')

    elif event == 'Cadastrar novo usuario':
        window = sg.Window('Cadastrar novo usuário')
