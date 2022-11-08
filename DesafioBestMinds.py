
import PySimpleGUI as sg
import smtplib #S M T P - Simple Mail Transfer Protocol
import email.message
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import random

#DESAFIO

#empresa Oliveira Trade e foi solicitado pelo board da empresa que seja desenvolvido uma
# forma de Sign in e Sign up de usuários.
# Devemos permitir que seja criado um usuário no sistema, com os campos mínimos de cadastro normal para Pessoa Física.
# O usuário deve ser notificado que o cadastro foi concluído com sucesso e, a partir deste ponto, ser possível executar login

def janela_sign_in(): #janela de Sign Up
    sg.theme('Reddit')
    layout = [
        [sg.Image(r'C:\Program Files\Desafio BestMinds\011-user (Custom).png'), sg.Text('Nome:')],
        [sg.Input(key='usuario', size=(43,1))],
        [sg.Image(r'C:\Program Files\Desafio BestMinds\012-lock (Custom).png'), sg.Text('Senha:')],
        [sg.Input(key='senha', password_char='*', size=(43,1))],
        [sg.Image(r'C:\Program Files\Desafio BestMinds\replock (Custom) .png'), sg.Text('Confirmar Senha:')],
        [sg.Input(key='repsenha', password_char='*', size=(43,1))],
        [sg.Image(r'C:\Program Files\Desafio BestMinds\082-credit_card (Custom).png'), sg.Text('CPF:')],
        [sg.Input(key='cpf', size=(43, 1))],
        [sg.Image(r'C:\Program Files\Desafio BestMinds\016-location (Custom).png'), sg.Text('Endereço:')],
        [sg.Input(key='endereco', size=(43, 1))],
        [sg.Image(r'C:\Program Files\Desafio BestMinds\017-phone (Custom).png'), sg.Text('Telefone:')],
        [sg.Input(key='telefone', size=(43, 1))],
        [sg.Image(r'C:\Program Files\Desafio BestMinds\013-mail (Custom).png'), sg.Text('E-mail:')],
        [sg.Input(key='e_mail', size=(43, 1))],
        [sg.Text('')],
        [sg.Button('Cadastrar'), sg.ProgressBar(10000, orientation='h', size=(21,1), border_width=4, key='progresso', bar_color=("Green", "Grey"))]

    ]

    return sg.Window('Sign In', layout=layout, finalize=True)

def janela_login(): #Janela de Sign In
    sg.theme('Reddit')
    layout = [
        [sg.Image(r'C:\Program Files\Desafio BestMinds\013-mail (Custom).png'), sg.Text('E-mail:'), sg.Input(key='email2', size=(21,1))],
        [sg.Image(r'C:\Program Files\Desafio BestMinds\012-lock (Custom).png'), sg.Text('Senha:'), sg.Input(key='senha', password_char='*', size=(21,1))],
        [sg.Checkbox('Salvar o Login', key='salvar')],
        [sg.Button('Entrar'), sg.Text('                     ') ,sg.Button('Novo Usuario', key='cadastrar2')],
    ]
    return sg.Window('Login', layout=layout, finalize=True)


def janela_home():
    sg.theme('Reddit')
    layout = [
        [sg.Text(f'Bem vindo {usuario}!!')],
        [sg.Text('Verifique o seu E-mail para confirmar os dados cadastrados.')]
    ]
    return sg.Window('Sucesso', layout=layout, finalize=True)


janela1, janela2, janela3, janela4 = janela_login(), None, None, None


e_mail = ''
senha = ''



def enviar_email():
    corpo_email = f"""
    <p>Olá, <b>{usuario}</b> seu cadastro foi efetuado com sucesso!!! </p>
    <p><b>🙍 Usuario:</b> {usuario} </p>
    <p><b>🔐 Senha:</b> {senha} </p> 
    <p><b>💳 CPF:</b> {cpf} </p>
    <p><b>📬 Endereço:</b> {end} </p>
    <p><b>📧 Email:<b> {e_mail} </p>
    <p><b>☎ Telefone:</b> {tel} </p>
    
    <p>Atenciosamente,</p>
    
   <p>Equipe,</p>
    
    <p>Oliveira Trade</p>
    <img src="https://raw.githubusercontent.com/AlexJ1Silva/DesafioBestMinds/main/Assinatura/assinatura%20(Custom).PNG"/>
    
    
    """


    msg = MIMEMultipart()
    msg['Subject'] = "Desafio BestMInds - EveryMInd"  # assunto do email.
    msg['From'] = 'testdesafio@gmail.com'    #seu email - email criado - testdesafio@gmail.com

    msg['To'] = f'{e_mail}'  #email destino #email que vai ser pego no input.
    password = 'pjsocmauivixnmoh' #Senha123
    msg.attach(MIMEText(corpo_email, 'html'))

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls() #Criar um grau de segurança
    # Login credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    s.quit()


def solve(s):
   pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   if re.match(pat,s):
      return True
   return False


while True:

    window, botoes, entrada = sg.read_all_windows()

    if window == janela1 and botoes == sg.WIN_CLOSED:
        break

    if window == janela1 and botoes == 'cadastrar2':
        janela1.hide()
        janela2 = janela_sign_in()

    if window == janela1 and botoes == 'Entrar':

        if entrada['email2'] == '' or entrada['senha'] == '':
            sg.popup('Preencha todos os campos.')

        elif not solve(entrada['email2']): #validação email
            sg.popup('E-mail invalido')

        elif entrada['email2'] == e_mail and entrada['senha'] == senha:
            sg.popup('Login Efetuado com Sucesso!')
            janela3 = janela_home()
            janela1.hide()
        else:

            sg.popup('Login ou Senha Incorretos Tente Novamente ou cadastre-se!')

    if window == janela2 and botoes == sg.WIN_CLOSED:
        break

    if window == janela2 and botoes == 'Cadastrar':

        usuario = entrada['usuario']
        senha = entrada['senha']
        r_senha = entrada['repsenha']
        cpf = '{}.{}.{}-{}'.format(entrada['cpf'][:3], entrada['cpf'][3:6], entrada['cpf'][6:9], entrada['cpf'][9:])
        end = entrada['endereco']
        tel ='({}) {}-{}'.format(entrada['telefone'][:2], entrada['telefone'][2:7], entrada['telefone'][7:11])
        e_mail = entrada['e_mail']

        if entrada['cpf'] == '' or entrada['endereco'] == '' or entrada['telefone'] == '' or entrada['e_mail'] == '': #validação campos vazios
            sg.popup('Preencha todos os campos.')
        elif entrada['senha'] != entrada['repsenha']: #validação das senhas
            sg.popup("As senhas não se coincidem")
        elif len(entrada['cpf']) != 11 or not entrada['cpf'].isdigit(): #validação do cpf
            sg.popup('Campo CPF: Formato errado. Tente de novo (apenas numeros)')
        elif len(entrada['telefone']) != 11 or not entrada['telefone'].isdigit(): #validação telefone
            sg.popup('Campo Telefone: Formato errado. Tente de novo (apenas numeros)')
        elif not solve(entrada['e_mail']): #validação email
            sg.popup('E-mail invalido')


        else:
            sg.popup('Aguarde alguns instantes.....')
            enviar_email()
            for i in range(10000):
                window['progresso'].update(i + 1)
            sg.popup('Enviamos um e-mail com seus dados para sua caixa de entrada.')
            sg.popup('Cadastro Efetuado com Sucesso!')
            janela2.hide()
            janela1 = janela_login()

    if window == janela3 and botoes == sg.WIN_CLOSED:
        break