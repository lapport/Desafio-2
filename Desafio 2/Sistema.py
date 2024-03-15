import webbrowser
from Interface.__init__ import *
from Dados.__init__ import *

cor = {'limpo': '\033[m',
       'branco': '\033[30m',
       'vermelho': '\033[31m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'azul': '\033[34m',
       'roxo': '\033[35m',
       'ciano': '\033[36m'}

while True:
    resposta = menu('Menu Principal',['Adicionar personagem', 'Ver pesonagem', 'Sair'])
    if resposta == 1:
        nome = input('Nome do personagem: ')
        descriçao = input('Descriçao do personagem:')
        link = input('Link: ')
        programa = input('Programa: ')
        animador = input('Animador: ')
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
