import PySimpleGUI as sg

sg.theme('Reddit')

def TelaInicial():
    src_image = r'PySimpleGui\img\logo.png'
    menu_layout = [['Pessoa', ['Cadastrar', 'Editar']],
                   ['Ajuda', ['Sobre']],
                   ]

    layout = [
        [sg.Image(src_image)],
        [sg.Menu(menu_layout)]
    ]

    window = sg.Window('Tela Inicial', layout)

    return window

    

def TelaCadastro():
    sg.Text('CADASTRO DE PESSOA') 

    layout = [
        [sg.Text('CPF:'),sg.Input( key='CPF', size=(20, 1)), sg.Text('Nome:'), sg.Input(key='Nome' , size=(30, 1))],
        [sg.Text('Endereço:'), sg.Input(key='Endereço', expand_x=True)],
        [sg.Text('Cidade:'), sg.Input(key='Cidade', size=(35,1)), sg.Text('Estado'), sg.Combo(['SP', 'RJ', 'MG', 'ES'], key='Estado', size=(20,1))],

        [sg.Frame('Sexo',
                  [[sg.Radio('Masculino', 'sexo', key='Masculino'),
                    sg.Radio('Feminino', 'sexo', key='Feminino'),]])],


        [sg.Text('E-mail', key='E-mail'), sg.Input(key='E-mail', size=(35,1)), sg.Text('Data de Nascimento:'), sg.Input(key='Data de Nascimento', size=(10,1))],        

        [sg.Text('Observações:'), sg.Multiline(size=(58, 5))],        

        [sg.Column(
        [[sg.Button('Cadastrar', size=(10, 2))]],
            element_justification='center',
            justification='center',
            vertical_alignment='center',
            k='-COL-'
    )]

    ]
    
    window2 = sg.Window('Cadastro de Pessoa', layout)

    return window2

while True:
    window = TelaInicial()

    event, values = window.read()
    

    if event == sg.WIN_CLOSED:
        break

    if event == 'Cadastrar':
        window.close()
        window2 = TelaCadastro()
        event, values = window2.read()
        

        if event == sg.WIN_CLOSED:
            break

        if event == 'Cadastrar':
            sg.popup('Usuário cadastrado com sucesso!')
            window2.close()
    
    
            






    








