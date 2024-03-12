import webbrowser
from Interface.__init__ import *
cor = {'limpo': '\033[m',
       'branco': '\033[30m',
       'vermelho': '\033[31m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'roxo': '\033[35m',
       'ciano': '\033[36m'}
lista = []

def adcicionar(nome, descriçao, link, programa, animador):
    personagem = {'Nome': nome,
                  'descriçao': descriçao,
                  'link': link,
                  'programa': programa,
                  'animador': animador}
    lista.append(personagem)


def mostrar(lista):
    print("\nLista de Personagens Cadastrados:")
    for idx, personagem in enumerate(lista, start=1):
        print(f"\nPersonagem {idx}:")
        for chave, valor in personagem.items():
            print(f"{chave}: {valor}")


def web(url):
    navegador = webbrowser.get()
    navegador.open(url)


while True:
    resposta = menu('Menu Principal',['Adicionar personagem', 'Ver pesonagem', 'Sair'])
    if resposta == 1:
        nome = input('Nome do personagem: ')
        descriçao = input('Descriçao do personagem:')
        link = input('Link: ')
        programa = input('Programa: ')
        animador = input('Animador')
        adcicionar(nome, descriçao, link, programa, animador)

    if resposta == 2:
        mostrar(lista)
        while True:    
            print('informe o numero do personagem: ')
            resposta = leiaint('Qual personagem deseja ver? ')
            if resposta > len(lista) or resposta < 0:
                print('DIGITE UM NUMERO VALIDO')
            else:
                url = lista[resposta-1]['link']
                web(url)
                break
    if resposta == 3:
        print('Finalizado')
        break