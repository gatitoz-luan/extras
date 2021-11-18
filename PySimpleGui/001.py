import PySimpleGUI as sg 
class TelaPython:
    sg.theme('dark grey 9')
    def __init__(self):
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0),key='nome')],
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(15,0),key='idade')],
            [sg.Text('Por onde deseja receber e-mail?')],
            [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Outlook',key='outlook'),sg.Checkbox('Yahoo',key='yahoo')],
            [sg. Text('Aceita cartão')],
            [sg. Radio('Sim','cartoes',key='aceitaCartao'),sg.Radio('Não','cartoes',key='naoaceitaCartao')],
            [sg. Text('Peso')],
            [sg.Slider(range=(0,250),default_value=0,orientation='h',size=(15,20),key='Peso')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30,20))]
        ]
        self.janela = sg.Window("Dados do Usuário").layout(layout)
        
    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook =self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao  = self.values['naoaceitaCartao']
            peso = self.values['Peso']
            print(f'Nome: {nome}')
            print(f'idade: {idade}')
            print(f'aceita gmail: {aceita_gmail}')
            print(f'aceita outlook: {aceita_outlook}')
            print(f'aceita yahoo: {aceita_yahoo}')
            print(f'aceita cartão: {aceita_cartao}')
            print(f'não aceita yahoo: {nao_aceita_cartao}')
            print(f'Velocidade Script: {peso}')

tela = TelaPython()
tela.Iniciar()
