import PySimpleGUI as sg

sg.theme('Reddit')

def TelaInicial():
    src_image = r'img\logo.png'
    menu_layout = [
        ['Pessoa', ['Cadastrar', 'Editar']],
        ['Ajuda', ['Sobre']]
    ]
    layout = [
        [sg.Image(src_image)],
        [sg.Menu(menu_layout)]
    ]
    window = sg.Window('Tela Inicial', layout)
    return window

def TelaCadastro():
     

    layout = [
        [sg.Column([[sg.Text('CADASTRO DE PESSOA')]], justification='center')],
        [sg.Text('CPF:'), sg.Input(key='CPF', size=(20, 1)), 
         sg.Text('Nome:'), sg.Input(key='Nome', size=(40, 1))],
        [sg.Text('Endereço:'), sg.Input(key='Endereço', expand_x=True)],
        [sg.Text('Cidade:'), sg.Input(key='Cidade', size=(35, 1)), sg.Text('Estado'), sg.Combo(['SP', 'RJ', 'MG', 'ES'], key='Estado', size=(20, 1))],
        [sg.Frame('Sexo', [[sg.Radio('Masculino', 'sexo', key='Masculino'), sg.Radio('Feminino', 'sexo', key='Feminino')]])],
        [sg.Text('E-mail'), sg.Input(key='E-mail', size=(35, 1)), sg.Text('Data de Nascimento:'), sg.Input(key='Data de Nascimento', size=(10, 1))],        
        [sg.Text('Observações:'), sg.Multiline(size=(58, 5), key='Observações')],        
        [sg.Column([[sg.Button('Cadastrar', size=(10, 2))]], element_justification='center', justification='center', vertical_alignment='center', k='-COL-')]
    ]
    
    window2 = sg.Window('Cadastro de Pessoa', layout)
    return window2

def editar():
    cabecalho = ['CPF', 'NOME', 'ENDEREÇO', 'CIDADE', 'ESTADO', 'SEXO', 'E-MAIL', 'DATA-DE-NASCIMENTO', 'OBSERVAÇÕES']

    layout = [
        [sg.Column([[sg.Text('PESSOAS CADASTRADAS')]], justification='center')],
        [sg.Column([[sg.Table(values=dados_usuarios, headings=cabecalho, justification='center', enable_click_events=True, key='-tabela-', display_row_numbers=True, auto_size_columns=True)]], justification='center')],
        [sg.Column([[sg.Button('Remover')]], justification='center')]
    ]
    window3 = sg.Window('Editando', layout=layout, finalize=True)

    while True:
        event, values = window3.read()

        if event == sg.WIN_CLOSED:
            break

        if event == 'Remover' and values['-tabela-']:
            # Remover o usuário selecionado da lista
            index = values['-tabela-'][0]
            del dados_usuarios[index]
            window3['-tabela-'].update(values=dados_usuarios)  # Atualiza a tabela após a remoção

    window3.close()

def sobre():
    autores = [
        ['Nome:', 'Rafael Almeida Vasconcelos'],
        ['Formação:', 'Engenharia de Software'],
        ['Cargo:', 'Gerente de Projetos'],
        ['Local de trabalho:', 'São Paulo'],
        ['Área de atuação:', 'Desenvolvimento de Software']
    ]

    cabecalho = ['Informação', 'Valor']

    layout = [
        [sg.Text('Informações sobre os Autores')],
        [sg.Listbox(values=[f'{item[0]} {item[1]}' for item in autores], size=(50, 6), disabled=True, enable_events=True, key='-LISTBOX-')],
        [sg.Button('Fechar')]
    ]

    window4 = sg.Window('Informações sobre os Autores', layout=layout)
    return window4

# Lista para armazenar os dados dos usuários cadastrados
dados_usuarios = []

while True:
    window = TelaInicial()
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Cadastrar':
        window.close()
        window2 = TelaCadastro()

        while True:
            event2, values2 = window2.read()

            if event2 == sg.WIN_CLOSED:
                break

            if event2 == 'Cadastrar':
                sg.popup('Usuário cadastrado com sucesso!')
                window2.close()
                pessoa = {
                    'CPF': values2.get('CPF'),
                    'Nome': values2.get('Nome'),
                    'Endereço': values2.get('Endereço'),
                    'Cidade': values2.get('Cidade'),
                    'Estado': values2.get('Estado'),
                    'Sexo': 'Masculino' if values2.get('Masculino') else 'Feminino',
                    'E-mail': values2.get('E-mail'),
                    'Data de Nascimento': values2.get('Data de Nascimento'),
                    'OBSERVAÇÕES': values2['Observações']
                }
                dados_usuarios.append(list(pessoa.values()))

    if event == 'Editar':
        window.close()
        editar()

    if event == 'Sobre':
        window.close()
        window4 = sobre()

        while True:
            event4, values4 = window4.read()

            if event4 == sg.WIN_CLOSED or event4 == 'Fechar':
                break

        window4.close()

window.close()