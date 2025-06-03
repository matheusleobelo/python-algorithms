grafo = {}
grafo['inicio'] = {}
grafo['inicio']['a'] = 6
grafo['inicio']['b'] = 2
grafo['a'] = {}
grafo['a']['fim'] = 1
grafo['b'] = {}
grafo['b']['a'] = 3
grafo['b']['fim'] = 5
grafo['fim'] = {}

# print(grafo['inicio'].keys())
# print(grafo['inicio']['a'])
# print(grafo['inicio']['b'])

infinito = float('inf')
custos = {}
custos['a'] = 6
custos['b'] = 2
custos['fim'] = infinito

pais = {}
pais['a'] = 'inicio'
pais['b'] = 'inicio'
pais['fim'] = None

processados = []

def acheNoCustoMaisBaixo(custos):
    custoMaisBaixo = float('inf')
    nodoCustoMaisBaixo = None
    for nodo in custos:
        custo = custos[nodo]
        if custo < custoMaisBaixo and nodo not in processados:
            custoMaisBaixo = custo
            nodoCustoMaisBaixo = nodo
    return nodoCustoMaisBaixo

nodo = acheNoCustoMaisBaixo(custos)
while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = nodo
    processados.append(nodo)
    nodo = acheNoCustoMaisBaixo(custos)

chave = 'fim'
lista = []

for i in range(3):
    for filho in pais:
        if filho == chave:
            lista.insert(0,filho)
            chave = pais[filho]

print(f'O tempo mínimo é: {custos["fim"]} minutos')
print(f"Seu caminho é: inicio")
for i in lista:
    print(f"Depois: {i}")

