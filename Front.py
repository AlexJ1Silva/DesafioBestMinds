
import PySimpleGUI as sg



#empresa Oliveira Trade e foi solicitado pelo board da empresa que seja desenvolvido uma
# forma de Sign in e Sign up de usuários.
# Devemos permitir que seja criado um usuário no sistema, com os campos mínimos de cadastro normal para Pessoa Física.
# O usuário deve ser notificado que o cadastro foi concluído com sucesso e, a partir deste ponto, ser possível executar login

def janela_sign_in(): #janela de Sign Up
    sg.theme('Reddit')
    layout = [
        [sg.Text('Usuario:'), sg.Input(key='usuario', size=(20,1))],
        [sg.Text('Senha:'), sg.Input(key='senha', password_char='*', size=(21,1))],
        [sg.Text('Confirmar Senha'), sg.Input(key='repsenha', password_char='*', size=(21,1))],
        [sg.Text('Informe seu CPF'), sg.Input(key='cpf', size=(21, 1))],
        [sg.Text('Informe seu Endereço'),sg.Input(key='endereco', size=(21, 1))],
        [sg.Text('Informe seu telefone'), sg.Input(key='telefone',size=(21, 1))],
        [sg.Text('E-mail'), sg.Input(key='email', size=(21, 1))],
        [sg.Button('Cadastrar')],
    ]
    return sg.Window('Sign In', layout=layout, finalize=True)

def janela_login(): #Janela de Sign In
    sg.theme('Reddit')
    layout = [
        [sg.Text('Usuario:'), sg.Input(key='usuario', size=(20,1))],
        [sg.Text('Senha:'), sg.Input(key='senha', password_char='*', size=(21,1))],
        [sg.Checkbox('Salvar o Login', key='salvar')],
        [sg.Button('Entrar')],
    ]
    return sg.Window('Login', layout=layout, finalize=True)


def janela_home(): #Janela de Sign In
    sg.theme('Reddit')
    layout = [
        [sg.Text('Bem Vindo:')],

    ]
    return sg.Window('Home', layout=layout, finalize=True)


janela1, janela2, janela3 = janela_sign_in(), None, None



while True:

    window, botoes, entrada, = sg.read_all_windows()
    if window == janela1 and botoes == sg.WIN_CLOSED:
        break

    if window == janela1 and botoes == 'Cadastrar':

        usuario = (entrada['usuario'])
        senha = (entrada['senha'])
        r_senha = (entrada['repsenha'])
        cpf = (entrada['cpf'])
        end = (entrada['endereco'])
        tel = (entrada['telefone'])
        email = (entrada['email'])

        if entrada['cpf'] == '' or entrada['endereco'] == '' or entrada['telefone'] == '' or entrada['email'] == '':
            sg.popup('Preencha todos os campos.')
        elif entrada['senha'] != entrada['repsenha']:
            sg.popup("As senhas não se coincidem")

        else:
            sg.popup('Cadastro Efetuado com Sucesso!')
            janela2 = janela_login()
            janela1.hide()


    if window == janela2 and botoes == sg.WIN_CLOSED:
        break

    if window == janela2 and botoes == 'Entrar':

        if entrada['usuario'] == usuario and entrada['senha'] == senha:
            sg.popup('Login Efetuado com Sucesso!')
            janela3 = janela_home()
            janela2.hide()
        else:

            sg.popup('Login ou Senha Incorretos Tente Novamente!')

    if window == janela3 and botoes == sg.WIN_CLOSED:
        break