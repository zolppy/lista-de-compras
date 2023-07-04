import os
import pickle # manipulação de arquivos
from enum import IntEnum

# enumerações tornam o código mais legível
class Menu(IntEnum):
    ADICIONAR_ITEM = 1
    EXIBIR_ITENS   = 2
    ATUALIZAR_ITEM = 3
    REMOVER_ITEM   = 4
    SAIR           = 5

# limpa o console de acordo com o sistema operacional
def limpar_console():
    if os.name == 'nt':  # windows
        os.system('cls')
    else:  # unix/linux/mac
        os.system('clear')

# carrega a lista de compras a partir do arquivo
def carregar_lista():
    if os.path.exists('dados.pkl'):
        with open('dados.pkl', 'rb') as arquivo:
            return pickle.load(arquivo)
    else:
        return []

# salva a lista de compras no arquivo
def salvar_lista(lista):
    with open('dados.pkl', 'wb') as arquivo:
        pickle.dump(lista, arquivo)

lista_compras = carregar_lista()

def adicionar_item():
    item = input('Digite o nome do item a ser adicionado: ')
    lista_compras.append(item)
    salvar_lista(lista_compras)
    print(f"Item '{item}' adicionado à lista de compras.")

def mostrar_itens():
    print('Lista de compras:')
    if lista_compras:
        for i, item in enumerate(lista_compras, start=1):
            print(f"{i}. {item}")
    else:
        print('A lista de compras está vazia.')

def atualizar_item():
    mostrar_itens()
    if lista_compras:
        indice = int(input('Digite o número do item a ser atualizado: '))
        if 1 <= indice <= len(lista_compras):
            novo_item = input('Digite o novo nome do item: ')
            lista_compras[indice - 1] = novo_item
            salvar_lista(lista_compras)
            print('Item atualizado com sucesso.')
        else:
            print('Índice inválido.')
    else:
        print('A lista de compras está vazia.')

def remover_item():
    mostrar_itens()
    if lista_compras:
        indice = int(input('Digite o número do item a ser removido: '))
        if 1 <= indice <= len(lista_compras):
            item_removido = lista_compras.pop(indice - 1)
            salvar_lista(lista_compras)
            print(f"Item '{item_removido}' removido da lista de compras.")
        else:
            print('Índice inválido.')
    else:
        print('A lista de compras está vazia.')

def exibir_menu():
    print('Menu:')
    print('1. Adicionar item')
    print('2. Mostrar itens')
    print('3. Atualizar item')
    print('4. Remover item')
    print('5. Sair')

while True:
    exibir_menu()
    opcao = int(input('Digite o número da operação desejada: '))

    if opcao == Menu.ADICIONAR_ITEM:
        limpar_console()
        adicionar_item()
    elif opcao == Menu.EXIBIR_ITENS:
        limpar_console()
        mostrar_itens()
    elif opcao == Menu.ATUALIZAR_ITEM:
        limpar_console()
        atualizar_item()
    elif opcao == Menu.REMOVER_ITEM:
        limpar_console()
        remover_item()
    elif opcao == Menu.SAIR:
        limpar_console()
        print('Até mais!')
        break
    else:
        print('Opção inválida. Tente novamente.')