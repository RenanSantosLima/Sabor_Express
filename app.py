import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Cafeteria', 'categoria': 'Italiana', 'ativo': False},
]

def exibir_nome_do_programa():
    '''Essa função é responsavel por mostrar o nome do programa na tela'''
    print('Sabor Express\n')

def exibir_opcoes():
    '''Essa função é responsavel por mostrar as opções na tela'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')


# função
def finalizar_app():
    '''Essa função é responsavel por finalizar o app'''
    exibir_subtitulo("Finalizando o app")

def voltar_ao_menu_principal():
    '''Solicita uma tecla para voltar ao menu principal
    
    -Outputs:
    Retorna ao menu principal 
    '''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def exibir_subtitulo(texto):
    '''Exibe um titulo estilizado na tela
    -Inputs:
    texto: str - texto do subtitulo
    '''
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    '''Exibi uma mesagem de opção invalida e retorna ao mune principal
    -Outputs:
    Retorna ao menu principal
    '''
    print("Opção invalida!")
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    '''Essa função é responsavel por cadastrar
    
    -Inputs:
    Nome do restaurante
    Categoria

    -Outputs:
    Adiciona um novo restaurante a lista de restaurantes
    
    '''
    exibir_subtitulo("Cadastrar novos restaurantes")

    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite o nome da categoria do {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')

    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função é responsavel por listar os restaurante
    -Outputs:
    Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo("Listando os restaurantes")

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Alterna o estado ativo/;desativado do restaurante
    -Input:
    Recebe o nome do restaurante

    -Output:
    Messgem de sucesso ou não na alteração
    '''
    exibir_subtitulo('Alternar estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
           restaurante_encontrado = True
           restaurante['ativo'] = not restaurante['ativo']
           mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
           print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()



def escolher_opcao():
    '''Solicita e executa a opção escolhida pelo usuário
    
    -Outputs
    Executa a opção escolhida pelo usuário
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # print(type(opcao_escolhida))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

    #match python versão 3.10 ou superior
    #match opcao_escolhida:
        #case 1:
            #print("Cadastrar restaurante")
        #case 2:
            #print("Listar restaurantes")
        #case 3:
            #print("Ativar restaurante")
        #case 4:
            #finalizar_app()
        #case _:
            #print("Opção invalida!")


# programa principal
def main():
    '''Função principal que inicia o programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()