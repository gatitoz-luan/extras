from time import sleep
import urllib.request
import webbrowser
try:
    urllib.request.urlopen("https://www.youtube.com/watch?v=ffbI0JMW7g4")
except Exception as erro:  # Desligando o wifi, ou o site não estiver no ar
    print('\033[1; 31mO melhor vídeo do youtube não está acessível no momento.\033[m')
    er = erro  # Variável usada para não ter marcações de erro no código.
else:  # Com wifi ligado:
    print('\033[1;32mConsegui acessar o link com sucesso!\033[m')
    print('Abrindo o youtube em 3, 2, 1...')
    sleep(3)
    webbrowser.open('https://www.youtube.com/watch?v=ffbI0JMW7g4', new=2)
    