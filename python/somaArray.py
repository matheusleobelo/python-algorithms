# def soma(lista):
#     total = 0
#     for item in lista:
#       total += item
#     return total

# print (soma([1,2,3,4]))

# def soma(lista):
#     if lista == []:
#         return 0
#     else:
#         inicio = lista.pop(0)
#     return inicio + soma(lista)

# print (soma([1,2,3,4]))

def conta(lista):
    if lista == []:
        return 0
    else:
        lista.pop(0)
    return 1 + conta(lista)

print (conta([1,2,3,4]))