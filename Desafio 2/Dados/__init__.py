
import webbrowser
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

adcicionar('Kauan', 'Antagonista','WWW','VSCODE','EU MESMO')
adcicionar('teste','Heroi','html','pycharm','ELE MESMO')
print(len(lista))




