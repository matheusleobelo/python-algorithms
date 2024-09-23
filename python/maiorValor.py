# def maiorValor(lista):
#     if len(lista) == 1:
#         return valor
#     else:
#         anterior = lista[0]
#         sucessor = lista[1]
#         if anterior >= sucessor:
#             lista.pop(1)
#             maiorValor(lista)
#             valor = anterior
#         else:
#             lista.pop(0)
#             maiorValor(lista)
#             valor = sucessor

# print (maiorValor([5,3,6,2,10]))        
    

def maiorValor(lista):
    if len(lista) == 1:
        return 0
    else:
        if lista[0] >= lista[1]:
            lista.pop(1)
            maiorValor(lista)
        else:
            lista.pop(0)
            maiorValor(lista)
    return lista[0]                    

print (maiorValor([17,5,3,6,2,10]))        
        