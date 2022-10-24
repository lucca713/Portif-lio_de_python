
import PySimpleGUI as sg   #aqui importou a bilbioteca do layout

layout = [
    [sg.Text('digite o nome do arquivo:'),sg.InputText(key='nome_arquivo')],  #aqui é o campo do layout
    [sg.Text('digite o nome do cliente:'),sg.InputText(key='nome_cliente')],
    [ sg.Text('digite a data ddmmyyyy:'),sg.InputText(key='data')],
    [ sg.Text('digite o produto:'),sg.InputText(key='produto')],
    [ sg.Text('digite o preço:'),sg.InputText(key='preco')],
    [sg.Button('lancar nota'), sg.Button('cancelar')],
]

janela = sg.Window('Nota Fiscal',layout)

while True:
    evento, valores = janela.read()


    if evento == sg.WIN_CLOSED or evento == 'cancelar':
        with open(filename, 'a') as file_object:
            file_object.write(f'O DIA ACABOU \n TOTAL DE VENDAS: {soma}\n') #quando clicar no cancelar ele manda o total do dia na nota

        break

    if evento == 'lancar nota':
        nome_arquivos = valores ['nome_arquivo'] #campos que recebem o imput que vao para a nota
        nome = valores ['nome_cliente']
        data = valores ['data']
        produtos = valores ['produto']
        preco = int(valores ['preco'])
        soma = preco
        filename = nome_arquivos

        with open(filename, 'a') as file_object: #aqui escreve na nota e cria uma arquito no pc com o nome da nota

            file_object.write(f'\n {nome}\n {data[0:2]}/{data[2:4]}/{data[4:8]}')

            soma += preco

            file_object.write(f'\n{produtos}: {preco}R$\n')




janela.close()