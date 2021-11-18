import PySimpleGUI as sg 

class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0))],
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(15,0))],
            [sg.Text('Por onde deseja receber e-mail?')]
            [sg.Checkbox('Gmail'),sg.Checkbox('Outlook'),sg.Checkbox('Yahoo')]
            [sg.Button('Enviar Dados')]
        ]
        janela = sg.Window("Dados do Usuário").layout(layout)
        self.button, self.value = janela.Read()
        
    def Iniciar(self):
        print(self.value)
        
tela = TelaPython()
tela.Iniciar()
