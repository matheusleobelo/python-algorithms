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
        custo = custos['nodo']
        if nodoCustoMaisBaixo>custo and nodo not in processados:
            custoMaisBaixo = custo
            nodoCustoMaisBaixo = nodo
    return nodoCustoMaisBaixo