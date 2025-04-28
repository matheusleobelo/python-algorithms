from collections import deque

grafo = {}
grafo['voce'] = ['alice', 'bob', 'claire']
grafo['bob'] = ['anuj','peggy']
grafo['alice'] = ['peggy']
grafo['claire'] = ['tom','jonny']
grafo['anuj'] = []
grafo['peggy'] = []
grafo['tom'] = []
grafo['jonny'] = []

def vendedorDeManga(nome):
    return nome[-1] == 'm'

def pesquisa(nome):
    filaDePesquisa = deque()
    filaDePesquisa += grafo[nome]
    verificados = []
    while filaDePesquisa:
        pessoa = filaDePesquisa.popleft()
        if pessoa not in verificados:
            if vendedorDeManga(pessoa):
                print(f"{pessoa} é um vendedor de manga")
                return True
            else:
                filaDePesquisa += grafo[pessoa]
                verificados.append(pessoa)
    return False

pesquisa('voce')