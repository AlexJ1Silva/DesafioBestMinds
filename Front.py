
import PySimpleGUI as sg
import smtplib
import email.message


#empresa Oliveira Trade e foi solicitado pelo board da empresa que seja desenvolvido uma
# forma de Sign in e Sign up de usuários.
# Devemos permitir que seja criado um usuário no sistema, com os campos mínimos de cadastro normal para Pessoa Física.
# O usuário deve ser notificado que o cadastro foi concluído com sucesso e, a partir deste ponto, ser possível executar login

def janela_sign_in(): #janela de Sign Up
    sg.theme('Reddit')
    layout = [
        [sg.Text('Usuario:'), sg.Input(key='usuario', size=(21,1),)],
        [sg.Text('Senha:'), sg.Input(key='senha', password_char='*', size=(21,1))],
        [sg.Text('Confirmar Senha'), sg.Input(key='repsenha', password_char='*', size=(21,1))],
        [sg.Text('Informe seu CPF'), sg.Input(key='cpf', size=(21, 1))],
        [sg.Text('Informe seu Endereço'),sg.Input(key='endereco', size=(21, 1))],
        [sg.Text('Informe seu telefone'), sg.Input(key='telefone',size=(21, 1))],
        [sg.Text('E-mail'), sg.Input(key='e_mail', size=(21, 1))],
        [sg.Button('Cadastrar')]

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


def janela_sucesso():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Cadastro Efetuado com Sucesso!!')],
    ]
    return sg.Window('Sucesso', layout=layout, finalize=True)


def janela_home(): #Janela de Sign In
    sg.theme('Reddit')
    layout = [
        [sg.Text('Bem Vindo:')],

    ]
    return sg.Window('Home', layout=layout, finalize=True)


janela1, janela2, janela3, janela4 = janela_sign_in(), None, None, None


def enviar_email():
    corpo_email = f"""
    Olá, {usuario} seu cadastro foi efetuado com sucesso!!! 
    Usuario: {usuario}
    Senha: {senha}  
    CPF: {cpf} 
    Endereço: {end}
    Email: {e_mail}
    Telefone: {tel} 
    
    Atenciosamente,
    
    Equipe,
    
    Oliveira Trade
    
    
    """


    msg = email.message.Message()
    msg['Subject'] = "Desafio BestMInds - EveryMInd"  # assunto do email.
    msg['From'] = 'testdesafio@gmail.com'    #seu email - email criado - testdesafio@gmail.com

    msg['To'] = 'ajs2mb@gmail.com'  #email destino #email que vai ser pego no input.
    password = 'pjsocmauivixnmoh' #Senha123
    msg.add_header('Content - Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls() #Criar um grau de segurança
    # Login credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))




while True:



    window, botoes, entrada = sg.read_all_windows()
    if window == janela1 and botoes == sg.WIN_CLOSED:
        break

    if window == janela1 and botoes == 'Cadastrar':

        usuario = (entrada['usuario'])
        senha = (entrada['senha'])
        r_senha = (entrada['repsenha'])
        cpf = (entrada['cpf'])
        end = (entrada['endereco'])
        tel = (entrada['telefone'])
        e_mail = (entrada['e_mail'])

        if entrada['cpf'] == '' or entrada['endereco'] == '' or entrada['telefone'] == '' or entrada['e_mail'] == '':
            sg.popup('Preencha todos os campos.')
        elif entrada['senha'] != entrada['repsenha']:
            sg.popup("As senhas não se coincidem")



        else:
            enviar_email()
            sg.popup('Cadastro Efetuado com Sucesso!')
            janela1.hide()
            janela2 = janela_login()





    if window == janela2 and botoes == sg.WIN_CLOSED:
        break

    if window == janela2 and botoes == 'Entrar':

        if entrada['usuario'] == usuario and entrada['senha'] == senha:
            sg.popup('Login Efetuado com Sucesso!')

            janela3 = janela_sucesso()
            janela2.hide()
        else:

            sg.popup('Login ou Senha Incorretos Tente Novamente!')

    if window == janela3 and botoes == sg.WIN_CLOSED:
        break